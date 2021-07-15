class Solution:
    # def __init__(self):
        # self.memo = {1: 0}
        
    def getPowVal(self, x: int) -> int:
        if x in self.memo:
            return self.memo[x]
        
        newX = x//2 if x%2==0 else 3*x+1
        
        self.memo[x] = 1 + self.getPowVal(newX)
        
        return self.memo[x]
#         intermed = []
#         steps = 0
#         while x != 1 or x not in self.memo:
#             intermed.append(x)
#             steps += 1
#             x = x//2 if x%2==0 else 3*x+1
        
#         if x in self.memo:
#             steps += self.memo[x]
        
#         for idx in range(len(intermed)):
#             self.memo[intermed[idx]] = steps-idx

        # return self.memo[intermed[0]]
    def getKth(self, lo: int, hi: int, k: int) -> int:
        self.memo = {1: 0}
        powVal = [ (x, self.getPowVal(x)) for x in range(lo, hi+1) ]
        
        powVal.sort(key=lambda x: x[1])
        

        return powVal[k-1][0]

