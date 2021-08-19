class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        # n = len(S)
        # zero = [0 for i in range(n)]
        # one = [0 for i in range(n)]
        # zero[0] = int(S[0])
        # one[0] = 1 - zero[0]
        # for i in range(1, n):
        #     if S[i] == '1':
        #         one[i] = min(one[i-1], zero[i-1])
        #         zero[i] = zero[i-1] + 1
        #     elif S[i] == '0':
        #         one[i] = min(one[i-1], zero[i-1]) + 1
        #         zero[i] = zero[i-1]
        # return min(zero[n-1], one[n-1])

        flip, one = 0, 0
        for i in S:
            if i == '1':
                one += 1
            else:
                flip += 1
            flip = min(one, flip)
        return flip
