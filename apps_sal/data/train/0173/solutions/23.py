class Solution:

    def canArrange(self, arr: List[int], k: int) -> bool:
        c = collections.Counter([a % k for a in arr])
        return all((c[i] == c[k - i] for i in range(1, k // 2 + 1))) and c[0] % 2 == 0
