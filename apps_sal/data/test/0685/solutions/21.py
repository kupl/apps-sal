(n, h) = [int(i) for i in input().split()]
A = [[int(i) for i in input().split()] for j in range(n)]
r = 0
cur_h = h
ans = 0
for l in range(n):
    while r < n - 1 and cur_h > A[r + 1][0] - A[r][1]:
        cur_h -= A[r + 1][0] - A[r][1]
        r += 1
    ans = max(ans, A[r][1] - A[l][0] + cur_h)
    if l < n - 1:
        cur_h += A[l + 1][0] - A[l][1]
print(ans)
