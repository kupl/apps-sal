n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
s = 0

ps = [0]
for i in a:
    ps.append(ps[-1] + i)

for j in range(k, n + 1):
    for i in range(n):
        if n < i + j:
            break
        s = max(s, (ps[i + j] - ps[i]) / j)

print(s)
