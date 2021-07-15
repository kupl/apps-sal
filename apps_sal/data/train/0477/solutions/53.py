vals = [0]
for _ in range(20):
    vals += [1] + [1-x for x in reversed(vals)]
    

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        return str(vals[k-1])
