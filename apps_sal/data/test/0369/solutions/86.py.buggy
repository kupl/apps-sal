N, M = list(map(int, input().split()))
S = list(reversed(input()))

ans = []
cur = 0
while cur < N:
    for m in range(M, 0, -1):
        ncur = cur + m
        if ncur <= N and S[ncur] == '0':
            ans.append(m)
            cur = ncur
            break
    else:
        print((-1))
        return

print((*reversed(ans)))
