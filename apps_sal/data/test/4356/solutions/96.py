n, m = map(int, input().split())
a = [[] for _ in range(n)]
b = ""
c = ""
ans = 0
for i in range(n):
    a[i] = list(input())
for j in range(m):
    b += input()
for i in range(n - m + 1):
    for j in range(n - m + 1):
        for k in range(i, i + m):
            for l in range(j, j + m):
                c += a[k][l]
        if c == b:
            ans += 1
            break
        c = ""
print("Yes" if ans > 0 else "No")
