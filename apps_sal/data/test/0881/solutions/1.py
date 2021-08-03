from sys import setrecursionlimit as srl
from functools import lru_cache
memo = lru_cache(None)
srl(10**5)
def rr(): return input().rstrip()
def rri(): return int(rr())
def rrm(): return list(map(int, rr().split()))


def solve(N, A):
    @memo
    def dp(i, j, left=0):
        if i == j:
            if left == 0:
                return 1
            if A[i] == left:
                return 1
            return 2
        if i > j:
            return 0 if left == 0 else 1
        # Try to greedy run up until left
        ans = 1 + dp(i + 1, j, A[i])
        if left >= 1:
            stack = []
            for k in range(i, j + 1):
                stack.append(A[k])

                while len(stack) >= 2 and stack[-1] == stack[-2]:
                    stack.pop()
                    stack[-1] += 1
                if len(stack) == 1 and left == stack[-1]:
                    cand = dp(k + 1, j, left + 1)
                    if cand < ans:
                        ans = cand
        return ans

    return dp(1, N - 1, A[0])


# print(solve(2,[2,2]))
# print(solve(3,[3,2,2]))
# print(solve(4,[3,2,2,3]))
# print(solve(5,[4,3,2,2,3]))
# print(solve(4,[4,3,2,2]))
#import random;random.seed(0);ri=random.randint
#print(solve(500, [ri(1,5) for _ in range(500)]))
print(solve(rri(), rrm()))
