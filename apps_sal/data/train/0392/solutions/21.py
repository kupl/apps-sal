class Solution:
    def numWays(self, s: str) -> int:
        n = len(s)
        
        
        #calculate count
        cnt = 0
        for i in s:
            if i == '1':
                cnt += 1
        if cnt%3 != 0:
            return 0
        
        partn = cnt/3
        
        
        range1_start = n+1
        range1 = [0,n-3]
        first = 0
        last = 0
        #calculate range1
        cnt = 0
        for idx, i in enumerate(s[:n-2]):
            if i == '1':
                cnt += 1
            
            if cnt == partn:
                if first == 0:
                    first = 1
                    range1[0] = idx
                
            if cnt > partn:
                if last == 0:
                    last = 1
                    range1[1] = idx-1
                
        
        #print(range1_low, range1_high)
        
        #calculate range2
        range2 = [range1[0]+1,n-2]
        first = 0
        last = 0
        cnt = 0

        for idx, i in enumerate(s[range2[0]:n]):
            if i == '1':
                cnt += 1
            
            if cnt == partn:
                if first == 0:
                    first = 1
                    range2[0] += idx 
                
            if cnt > partn:
                if last == 0:
                    last = 1
                    range2[1] = range1[0] + idx
                
        
        #print(range2_low, range2_high)
#         print(range1, range2)       
        
        total = 0
        modulo = pow(10,9) + 7
        for i in range(range1[0], range1[1]+1):
            j = range2[0]
            if i<j and i<n and j<n:
                add = (range2[1] - range2[0] + 1)
                total += add%modulo
                #print(add, total)
            else:
                total += (range2[1] - i)%modulo
        # print(total)
        total =  total%modulo
        # print(total)
        return total
