class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        prefix_sum = [0]
        for idx, i in enumerate(A):
            prefix_sum.append(i + prefix_sum[idx])
        print(prefix_sum)

        num_enc = dict()
        total = 0
        for i in prefix_sum:
            if (i % K) in num_enc:
                total += num_enc[i % K]
            if (i % K - K) in num_enc:
                total += num_enc[i % K - K]
            if i % K not in num_enc:
                num_enc[i % K] = 0
            num_enc[i % K] += 1
        return total
