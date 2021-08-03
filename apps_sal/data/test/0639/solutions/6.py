n, x = map(int, input().split())

l = [1] * 101

for v in map(int, input().split()):
    l[v] = 0

ans = int(not l[x])

for i in range(x):
    ans += l[i]

print(ans)
