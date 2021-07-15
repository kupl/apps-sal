# factorials = [1]

# def choose(n,r):
#     nonlocal factorials
#     return factorials[n]/(factorials[n-r]*factorials[r])

# def counter(d,f,target,facesUsed, d_og, t_og):
#     if(d==0 and target==0):
#         return factorials[d_og]
#     if(d<0 or target<0 or f<1):
#         return 0
#     # print(d,f,target,facesUsed, min(target//f + 1,d))
#     c = 0
#     for i in range(min(target//f,d)+1):
#         a = counter(d-i,f-1,target-f*i,facesUsed + 0 if i==0 else 1,d_og,t_og) / factorials[i]
#         c += a
#     return c
        
class Solution:    
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # nonlocal factorials
        # for i in range(1,d+1):
        #     factorials.append(i*factorials[i-1])
        # return int(counter(d,f,target,0,d,target))
        dpt = [[1 if (i == 0 and 0<j and j <= f) else 0 for j in range(target+1)] for i in range(d)]
        # for i in range(d):
            # for j in range(min(,target):
        for i in range(1,d):
            for j in range(1,target+1):
                for k in range(1,f+1):
                    if(j-k >= 0):
                        dpt[i][j] += dpt[i-1][j-k] % (10**9+7)
        # print(dpt)
        return dpt[-1][target] % (10**9+7)
        

