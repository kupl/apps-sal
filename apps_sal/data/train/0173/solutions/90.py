from collections import Counter


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        counter = Counter([num % k for num in arr])
        return all([counter[i] == counter[k - i] for i in range(1, k // 2 + 1)]) and counter[0] % 2 == 0
