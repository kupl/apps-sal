from bisect import bisect_left

N, M = list(map(int, input().split()))
S = [i for i, s in enumerate(input()) if s == '0']

ans = []
now = N
while now > 0:
    nxI = bisect_left(S, now - M)
    nx = S[nxI]

    if nx == now:
        print((-1))
        return

    ans.append(now - nx)
    now = nx

print((*ans[::-1]))
