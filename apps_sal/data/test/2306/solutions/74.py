n = int(input())
t = [int(i) for i in input().split()]
v = [int(i) for i in input().split()]
l = []

for i in range(n):
    l += [v[i]] * t[i] * 2

l = [min(i, j) for i, j in zip([0] + l, l + [0])]

for i in range(1, len(l)):
    l[i] = min(l[i], l[i - 1] + 0.5)
for i in range(len(l) - 1)[::-1]:
    l[i] = min(l[i], l[i + 1] + 0.5)

ans = 0

for i in range(1, len(l)):
    ans += 0.25 * (l[i] + l[i - 1])

print(ans)
