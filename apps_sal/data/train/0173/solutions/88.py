class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d = {i: 0 for i in range(k)}
        for num in arr:
            d[num % k] += 1
        if d[0] % 2 != 0:
            return False
        for i in range(1, k):
            if i != k - i:
                if d[i] != d[k - i]:
                    return False
            else:
                if d[i] % 2 != 0:
                    return False

        return True
