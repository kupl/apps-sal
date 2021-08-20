(N, M) = map(int, input().split())
A = []
for _ in range(N):
    KA = list(map(int, input().split()))
    A.append(KA[1:])
ans = [0] * M
for a in A:
    for i in a:
        ans[i - 1] += 1
print(ans.count(N))
