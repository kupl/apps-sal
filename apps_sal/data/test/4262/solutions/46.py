from math import factorial as fac
N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))


def F(List):
    ans = 1
    L = len(List)
    nums = list(range(1, N + 1))
    for i in range(L):
        ans += fac(L - i - 1) * nums.index(List[i])
        nums.remove(List[i])
    return ans


print(abs(F(P) - F(Q)))
