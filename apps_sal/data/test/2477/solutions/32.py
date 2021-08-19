import math
(N, K) = map(int, input().split())
A = list(map(int, input().split()))


def judge(ans, K, A):
    cut = 0
    for i in range(len(A)):
        cut += (A[i] - 1) // ans
    if cut > K:
        return False
    else:
        return True


ansp = max(A)
ansm = 0
ans = (ansp + ansm) // 2
d = 1
while ansp - ansm > d:
    if judge(ans, K, A):
        ansp = ans
    else:
        ansm = ans
    ans = (ansp + ansm) // 2
print(ansp)
