n = int(input())
l = [0] * n
r = [0] * n
for i in range(n):
    l[i], r[i] = map(int, input().split())
res = 0

for i in range(n):
    res += r[i] - l[i] + 1

print(res)
