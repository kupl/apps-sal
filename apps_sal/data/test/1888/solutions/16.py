(n, m) = list(map(int, input().split()))
debt = [0] * (n + 1)
for i in range(m):
    (a, b, c) = list(map(int, input().split()))
    debt[a] -= c
    debt[b] += c
ans = 0
for i in debt:
    if i > 0:
        ans += i
print(ans)
