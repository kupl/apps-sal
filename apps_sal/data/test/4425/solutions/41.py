r = input().split()
N = int(r[0])
K = int(r[1])
ans = 0
for i in range(1, N + 1):
    x = i
    n = 0
    while x <= K - 1:
        x = x * 2
        n += 1
    ans += 1 / N * (1 / 2) ** n
print(ans)
