n = int(input())
a_ls = list(map(int, input().split()))
r = 0
ans = 0
S = a_ls[0]
for l in range(n):
    if l == r and S == 0:
        S = a_ls[l]
    while r + 1 < n and S+a_ls[r+1] == S^a_ls[r+1]:
        S += a_ls[r+1]
        r += 1
    ans += r - l + 1
    if r == l:
        r += 1
    S -= a_ls[l]
print(ans)


