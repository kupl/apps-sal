(N, M) = map(int, input().split())
A = list(map(int, input().split()))
res = []
for i in A:
    if i >= sum(A) / (4 * M):
        res.append(i)
if len(res) >= M:
    print('Yes')
else:
    print('No')
