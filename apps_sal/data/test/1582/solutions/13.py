N = int(input())
c = [[0 for i in range(10)] for j in range(10)]

for n in range(1, N + 1):
    i = int(str(n)[0])
    j = int(str(n)[-1])
    c[i][j] += 1

ans = 0
for i in range(10):
    for j in range(10):
        ans += c[i][j] * c[j][i]
print(ans)
