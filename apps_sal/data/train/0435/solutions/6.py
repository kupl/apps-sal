class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        cumsum = [0]
        for n in A:
            cumsum.append(cumsum[-1] + n)
        print((cumsum, A))
        cnt = 0
        # for i in range(len(A)):
        #     for j in range(i+1,len(A)):
        #         if (cumsum[j]-cumsum[i])%K == 0:
        #             cnt += 1
        # return cnt
        count = [0] * K
        for x in cumsum:
            count[(x % K + K) % K] += 1

        cnt = 0
        for num in count:
            cnt += num * (num - 1) // 2
        return cnt
