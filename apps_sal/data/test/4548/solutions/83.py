N, M, X = list(map(int, input().split()))
A = list(map(int, input().split()))

for i, a in enumerate(A):
    if X < a:
        break

if i > len(A) / 2:
    ans = len(A[i:])
else:
    ans = len(A[:i])

print(ans)
