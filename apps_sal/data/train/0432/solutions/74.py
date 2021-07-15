class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        M: Mapping[int, int] = {}
        for n in nums:
            if n in M:
                M[n] = M[n]+1
            else:
                M[n] = 1

        n = sorted(M.keys())[0]
        while True:
            for i in range(k):
                if n not in M or M[n] == 0:
                    return False
                M[n] = M[n] - 1
                n = n + 1

            for n in list(M.keys()):
                if M[n] == 0:
                    del (M[n])

            if len(list(M.keys())) == 0:
                return True

            n = sorted(M.keys())[0]

