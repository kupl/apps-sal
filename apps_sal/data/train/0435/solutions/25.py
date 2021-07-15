class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        n = len(A)
        prefix = [0] * (n+1)
        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + A[i-1]
        for i in range(1, n+1):
            prefix[i] = prefix[i] % K
        d = defaultdict(list)
        ans = 0
        for i in range(1, n+1):
            if prefix[i] == 0:
                ans += 1
            if prefix[i] in d.keys():
                ans += len(d[prefix[i]])
            d[prefix[i]].append(i)
        return ans
