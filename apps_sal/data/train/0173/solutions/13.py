from collections import Counter

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainders = [0 for _ in range(k)]
        for number in arr:
            rem = number % k
            remainders[rem] += 1
        for i in range(k):
            if i == 0:
                if remainders[0] % 2 != 0:
                    return False
                continue
            if remainders[i] != remainders[k-i]:
                return False
        return True
