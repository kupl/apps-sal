class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d = [0] * k
        for i in range(len(arr)):
            d[arr[i] % k] += 1
        for i in range(len(d)):
            if i == 0:
                if d[i] % 2 != 0:
                    return False
            else:
                if d[i] != d[k - i]:
                    return False
        return True
