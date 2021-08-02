n, m = [int(x) for x in input().split()]
arr = [[int(x) for x in input().split()]for i in range(0, n)]
v = [[1] * m for i in range(0, n)]  # a 2d array of size [n][m]
for i in range(0, m):
    for j in range(1, n):
        if(arr[j][i] >= arr[j - 1][i]):
            v[j][i] = v[j - 1][i] + 1  # if in increasing order increase value by 1

best = [max(i) for i in v]  # to store largest value in row
ans = ""
t = int(input())
for i in range(0, t):
    x, y = [int(s) for s in input().split()]
    if(best[y - 1] >= y - x + 1):  # compare that largest value
        ans += "Yes\n"
    else:
        ans += "No\n"

print(ans)
