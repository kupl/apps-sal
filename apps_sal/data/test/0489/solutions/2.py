import math


def newton(n, k):
    if k == n:
        return 1
    if k == 1:
        return n
    if k > n:
        return 0
    a = math.factorial(n)
    b = math.factorial(k)
    c = math.factorial(n - k)
    return (a // (b * c))


n = int(input())

S = dict()

L = sorted(list(map(int, input().split())))

for e in L:
    if e in S:
        S[e] += 1
    else:
        S[e] = 1

L = sorted(set(L))


cnt = 0
cnt2 = 0
for e in L:
    cnt += S[e]
    if cnt >= 3:
        print(newton(S[e], S[e] - (3 - cnt2)))
        break
    cnt2 += S[e]
