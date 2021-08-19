(n, k) = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort(reverse=True, key=lambda x: x % 10)
for (i, a) in enumerate(A):
    if k <= 0 or a % 10 == 0:
        break
    new = min(k, 10 - a % 10, 100 - a)
    A[i] += new
    k -= new
if k:
    for (i, a) in enumerate(A):
        if k <= 0:
            break
        new = min(100 - a, k)
        A[i] += new
        k -= new
ans = sum((a // 10 for a in A))
print(ans)
