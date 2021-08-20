A = list(map(int, input().split()))
A.sort()
ans = 0
count = [0, 0]
for a in A:
    if a & 1:
        count[1] += 1
    else:
        count[0] += 1
if count[0] == 0 or count[1] == 0:
    m = A[2]
    ans += 3 * m - sum(A)
    ans //= 2
elif A[1] - A[0] & 1:
    m = A[2] + 1
    ans += 3 * m - sum(A)
    ans //= 2
else:
    m = A[2]
    ans += 3 * m - sum(A)
    ans //= 2
print(ans)
