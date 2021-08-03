class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if len(arr) % 2 != 0:
            return False
        lookup = [0] * k
        for num in arr:
            lookup[num % k] += 1

        if lookup[0] % 2 != 0:
            return False
        for p in range(1, k):
            if p != k - p:
                if lookup[p] != lookup[k - p]:
                    return False
            else:
                if lookup[p] % 2 != 0:
                    return False
        return True
