n, x = map(int, input().split())
m = []
for i in range(n):
    m.append(int(input()))
ans = 0

x -= sum(m)
ans += n
ans += x // min(m)

print(ans)
