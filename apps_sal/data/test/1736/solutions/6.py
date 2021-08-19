(n, t) = list(map(int, input().split()))
A = list(map(int, input().split()))
ans = 0
ind = 0
best = 0
for i in range(n):
    if i >= ind:
        ind = i
        ans = 0
    while ind < n and t >= A[ind]:
        ans += 1
        t -= A[ind]
        ind += 1
    if ans > best:
        best = ans
    if ind == n:
        break
    if ind != i:
        t += A[i]
        ans -= 1
print(best)
