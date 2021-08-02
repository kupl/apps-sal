l, r = map(int, input().split())
s = set()

for x in range(35):
    for y in range(35):
        if (2 ** x) * (3 ** y) <= 2000000000:
            s.add((2 ** x) * (3 ** y))

ans = 0
for x in s:
    if l <= x and x <= r:
        ans += 1

print(ans)
