class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        st = {}
        A = sorted(A,reverse=True)
        for i in A:
            if i in st:st[i]+=1
            else: st[i] = 1
        #print(st)
        for num in A:
            if (num*2) in st and st[num] > 0 and st[(num*2)] > 0:
                st[num*2]-=1
                st[num]-=1
            #print(num,st)
        for num in st:
            if st[num] > 0:return False
        return True

