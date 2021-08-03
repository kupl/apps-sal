n = int(input())

a = list(map(int, input().split()))

d = {}

for c in a:
    d[c] = d.get(c, 0) + 1

b = []

mx = 0

for c in d:
    ans = 0
    for i in range(0, 6):
        ans += d.get(c + i, 0)
    if ans > mx:
        mx = ans

print(mx)
