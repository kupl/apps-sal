(n, m) = list(map(int, input().split()))
ip = list(map(int, input().split()))
ans = 0
for i in range(m):
    (a, b) = list(map(int, input().split()))
    s = 0
    a -= 1
    b -= 1
    for j in range(a, b + 1):
        s += ip[j]
    if s > 0:
        ans += s
print(ans)
