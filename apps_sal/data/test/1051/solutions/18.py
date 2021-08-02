3

k = int(input())
a = set(map(int, input().split()))

c = 1
while len(a) < 25:
    if c not in a:
        a.add(c)
    else:
        c += 1

b = list(a)
b.sort()

ans = 0
y = 0
for x in b:
    ans += x - y - 1
    y = x

print(ans)
