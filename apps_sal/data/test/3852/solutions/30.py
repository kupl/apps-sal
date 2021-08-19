N = int(input())
A = list(map(int, input().split()))
mx = max(A)
mxi = A.index(mx)
mn = min(A)
mni = A.index(mn)
ans = []
if mn >= 0 or mx + mn >= 0:
    for i in range(N):
        if A[i] < 0:
            ans.append((mxi, i))
    for i in range(N - 1):
        ans.append((i, i + 1))
else:
    for i in range(N):
        if A[i] > 0:
            ans.append((mni, i))
    for i in range(N - 1, 0, -1):
        ans.append((i, i - 1))
print(len(ans))
for (a, b) in ans:
    print(a + 1, b + 1)
