class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        mem = {}
        gsizes = 0
        inc = False
        lastpos = -1
        changed = False
        
        for i, num in enumerate(arr):
            # print(mem)
            gsize = 1
            if num -1 in mem:
                if mem[num-1][0] == m:
                    gsizes -= 1
                    changed = True
                gsize += mem[num-1][0]
            
            if num +1 in mem:
                if mem[num+1][0] == m:
                    gsizes -= 1
                    changed = True
                gsize += mem[num+1][0]
            
            # print(gsize, m)
            if gsize == m:
                inc = True
                changed = True
                gsizes += 1
            # print(gsizes)

            # print(mem)
            # if inc:
            #     print(gsizes)
            #     print(gsize)
            #     print(num)
            
            # print(gsizes)
            if gsizes == 0 and inc and changed:
                changed = False
                lastpos = i
                # print('end')
                # return i
            
            # mem[num] = (gsize, num)
            if num +1 not in mem and num -1 not in mem:
                end = num
            elif num + 1 in mem:
                end = mem[num+1][1]
            else:
                end = mem[num-1][1]
            mem[num] = (gsize, end)
            
            if num - 1 in mem:
                old = mem[num-1][1]
                mem[mem[num-1][1]] = (gsize, mem[num+1][1] if num +1 in mem else num)
                
            if num + 1 in mem:
                mem[mem[num+1][1]] = (gsize, old if num -1 in mem else num)
                
#         if gsizes:
#             return len(arr)
        # print(gsizes)
            
        # return -1 if gsizes == 0 else len(arr)
        return len(arr) if gsizes else lastpos
        
            
                

