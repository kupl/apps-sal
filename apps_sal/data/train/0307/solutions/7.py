class Solution:
    def soupServings(self, N: int) -> float:
        # 4,0
        # 3,1
        # 2,2
        # 1,3
        if N % 25 == 0:
            N = N // 25
        else:
            N = (N // 25) + 1

        solA = {}
        solB = {}

        def solutionA(a, b):
            if a == 0 and b > 0:
                return 1
            elif a == 0 and b == 0:
                return 0
            elif a > 0 and b == 0:
                return 0
            else:
                if (a, b) in solA:
                    return solA[(a, b)]
                else:
                    solA[(a, b)] = 0.25 * (solutionA(max(a - 4, 0), b) + solutionA(max(a - 3, 0), max(b - 1, 0)) + solutionA(max(a - 2, 0), max(b - 2, 0)) + solutionA(max(a - 1, 0), max(b - 3, 0)))
                    return solA[(a, b)]

        def solutionB(a, b):
            if a == 0 and b == 0:
                return 1
            elif a == 0 or b == 0:
                return 0
            else:
                if (a, b) in solB:
                    return solB[(a, b)]
                else:
                    solB[(a, b)] = 0.25 * (solutionB(max(a - 4, 0), b) + solutionB(max(a - 3, 0), max(b - 1, 0)) + solutionB(max(a - 2, 0), max(b - 2, 0)) + solutionB(max(a - 1, 0), max(b - 3, 0)))
                    return solB[(a, b)]

        if N > 300:
            return 1
        else:
            return solutionA(N, N) + 0.5 * solutionB(N, N)
