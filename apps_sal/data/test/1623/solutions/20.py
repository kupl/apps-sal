
ln = [int(i) for i in input().split(" ")]
n = ln[0]
l = ln[1]
r = ln[2]

ms = (n - l + 1)
t = 1
for i in range(n - l + 1, n):
    ms += 2 ** t
    t += 1

mx = 0
t = 0

for i in range(0, r):
    mx += 2 ** t
    t += 1

t -= 1

mx += (2 ** t) * (n - r)

print(ms, mx)
