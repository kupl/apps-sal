n = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
k = 0
for i in range(2):
    c.append([0] * n)
c[1][0] = b[0]
for i in range(1, n):
    c[0][i] = c[0][i - 1] + a1[i - 1]
    if c[1][i - 1] + a2[i - 1] > c[0][i] + b[i]:
        k = i
    c[1][i] = min(c[1][i - 1] + a2[i - 1], c[0][i] + b[i])
ans = 0
ans += c[-1][-1]
b[k] = 1000
c = []
for i in range(2):
    c.append([0] * n)
c[1][0] = b[0]
for i in range(1, n):
    c[0][i] = c[0][i - 1] + a1[i - 1]
    c[1][i] = min(c[1][i - 1] + a2[i - 1], c[0][i] + b[i])
ans += c[-1][-1]
print(ans)
