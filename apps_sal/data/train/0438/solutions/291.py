class Solution:
    def findLatestStep(self, arr, m):
        D = dict() # D[x] records the index of the end in the interval, +: right end, -: left end
        
        c, ret = 0, -1 # c: count of m-intervals, ret: return index
        for k, x in enumerate(arr, 1):
            D[x], S = 0, 0 # S: shift
            
            # discuss in cases
            if x-1 in D and x+1 in D:
                i, j = D[x-1], -D[x+1]
                if i+1 == m: # i+1 is the length
                    c -= 1
                if j+1 == m:
                    c -= 1
                S = i+j+2
                D[x-i-1], D[x+j+1] = -S, S
            elif x-1 in D:
                i = D[x-1]
                if i+1 == m:
                    c -= 1
                S = i+1
                D[x-i-1], D[x] = -S, S
            elif x+1 in D:
                j = -D[x+1]
                if j+1 == m:
                    c -= 1
                S = j+1
                D[x+j+1], D[x] = S, -S
                
            if S+1 == m: # find a m-inteval
                c += 1
            if c > 0: # no m-interval in this round
                ret = k
        
        return ret
