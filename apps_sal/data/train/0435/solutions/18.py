class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        prefix = [0]*len(A)
        prefix[0] = A[0]%K
        counter = Counter([prefix[0]])
        ans = 1 if prefix[0] == 0 else 0
        for i in range(1, len(A)):
            prefix[i] = (prefix[i-1] + A[i]) % K
            target = prefix[i] - 0
            ans += counter[target]
            if target == 0:
                ans += 1
            counter[prefix[i]] += 1
        return ans
