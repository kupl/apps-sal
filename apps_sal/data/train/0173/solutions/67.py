class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if len(arr) == 0: return False
        if len(arr) % 2 != 0: return False
        Check = dict()
        for i in range(len(arr)):
            if arr[i] % k not in Check:
                Check[arr[i] % k] = 0
            Check[arr[i] % k] += 1
        if 0 in Check and Check[0] % 2 != 0: 
            return False
        for i in range(1,k):
            if i in Check:
                if k - i not in Check or Check[i] != Check[k-i]:
                    return False
        return True

