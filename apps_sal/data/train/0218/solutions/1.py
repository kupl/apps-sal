class Solution:
    def orderlyQueue(self, S: str, K: int) -> str:
        if K == 1:
            tmp = S
            for i in range(len(S)):
                S = S[1:] + str(S[0])
                if S < tmp:
                    tmp = S
            return tmp
        else:
            return ''.join(sorted(S))
