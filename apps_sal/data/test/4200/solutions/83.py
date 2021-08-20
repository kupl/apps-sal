(N, M) = map(int, input().split())
A_l = sorted(map(int, input().split()))
S = sum(A_l)
ans = 0
for i in range(N):
    if A_l[i] * 4 * M >= S:
        ans += 1
    else:
        continue
if ans >= M:
    print('Yes')
else:
    print('No')
