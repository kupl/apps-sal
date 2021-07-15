from math import factorial
def c(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))
    
n, m = map(int, input().split())
ans = 0
a = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    c0, c1 = 0, 0
    for j in range(m):
        if a[i][j]:
            c1 += 1
        else:
            c0 += 1
    for j in range(1, c0 + 1):
        ans += c(c0, j)
    for j in range(1, c1 + 1):
        ans += c(c1, j)
for j in range(m):
    c0, c1 = 0, 0
    for i in range(n):
        if a[i][j]:
            c1 += 1
        else:
            c0 += 1
    for i in range(2, c0 + 1):
        ans += c(c0, i)
    for i in range(2, c1 + 1):
        ans += c(c1, i)
print(ans)
