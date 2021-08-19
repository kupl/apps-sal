n = int(input())
arr = [list(input()) for i in range(n)]
ans = 0
for i in arr:
    s = 0
    for j in i:
        if j == 'C':
            s += 1
    ans += s * (s - 1) // 2
for i in range(n):
    s = 0
    for j in range(n):
        if arr[j][i] == 'C':
            s += 1
    ans += s * (s - 1) // 2
print(ans)
