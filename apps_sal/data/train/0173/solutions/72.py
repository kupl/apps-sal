class Solution:

    def canArrange(self, arr: List[int], k: int) -> bool:
        arr = sorted([c % k for c in arr])
        count = Counter(arr)
        for i in range(len(arr) // 2):
            if count[arr[i]] > 0:
                count[arr[i]] -= 1
                if count[(k - arr[i]) % k] == 0:
                    return False
                else:
                    count[(k - arr[i]) % k] -= 1
        return True
