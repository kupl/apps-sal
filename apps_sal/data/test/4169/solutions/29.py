(n, m) = list(map(int, input().split()))
lis = []
ans = 0
for _ in range(n):
    (A, B) = list(map(int, input().split()))
    lis.append((A, B))
lis.sort()
for x in lis:
    (a, b) = x
    if m >= b:
        m -= b
        ans = ans + a * b
    else:
        ans = ans + a * m
        break
print(ans)
