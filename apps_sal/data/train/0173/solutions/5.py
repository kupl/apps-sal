class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        recDict = {}
        for i in range(0, k):
            recDict[i] = 0
        for i in arr:
            recDict[i%k] += 1
        for i in range(1, k):
            if recDict[i] !=recDict[k-i]:
                return False
        if recDict[0]%2 !=0:
            return False
        return True

