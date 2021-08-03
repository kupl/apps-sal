import sys
input = sys.stdin.readline

m, n, k, t = list(map(int, input().split()))
A = list(map(int, input().split()))
T = [tuple(map(int, input().split())) for i in range(k)]

A.sort(reverse=True)

SLIST = [0] * (2 * 10**5 + 2)

ind = 0
for i in range(A[0], -1, -1):
    SLIST[i] = SLIST[i + 1]

    while ind < m and A[ind] == i:
        SLIST[i] += 1
        ind += 1

SLIST = [SLIST[0]] + SLIST

NG = 0
OK = 2 * 10**5 + 1

while OK - NG > 1:
    mid = (OK + NG) // 2

    USE = [0] * (2 * 10**5 + 3)

    for l, r, d in T:
        if d >= mid:
            USE[l - 1] += 1
            USE[r] -= 1

    for i in range(1, 2 * 10**5 + 3):
        USE[i] += USE[i - 1]

    # print(mid,USE[:10],(2*10**5+3-USE.count(0))*2+n+1)

    if (2 * 10**5 + 3 - USE.count(0)) * 2 + n + 1 <= t:
        OK = mid
    else:
        NG = mid

print(SLIST[OK])
