class Solution:

    def canArrange(self, arr: List[int], k: int) -> bool:
        arr = [a % k for a in arr]
        arr = Counter(arr)
        if arr.get(0, 0) % 2 != 0:
            return False
        if k % 2 == 0 and arr.get(k / 2, 0) % 2 == 1:
            return False
        i = 1
        k -= 1
        while k > i:
            if arr.get(k, 0) != arr.get(i, 0):
                return False
            i += 1
            k -= 1
        return True
