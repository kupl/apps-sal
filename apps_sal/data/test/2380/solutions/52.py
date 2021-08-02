n, m = map(int, input().split())
A = list(map(int, input().split()))
D = [(A[i], 1) for i in range(n)]

for i in range(m):
    b, c = map(int, input().split())
    D.append((c, b))

D.sort(reverse=True)

ans, left = 0, n

for (i, j) in D:
    use = min(j, left)
    ans += use * i
    left -= use
print(ans)
