class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:

        arr = [a % k for a in arr]
        arr.sort()

        arr = [a for a in arr if a != 0]
        if len(arr) % 2 == 1:
            return False

        l, r = 0, len(arr) - 1

        while l < r:
            if arr[l] + arr[r] != k:
                return False
            r -= 1
            l += 1

        return True
