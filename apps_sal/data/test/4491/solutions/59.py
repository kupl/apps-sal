n = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))

for i in range(1, n):
    a1[i] += a1[i - 1]

for i in range(n - 2, -1, -1):
    a2[i] += a2[i + 1]

res = 0
for i in range(n):
    tmp = a1[i] + a2[i]
    res = max(tmp, res)

print(res)
