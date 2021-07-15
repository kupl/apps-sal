n = int(input())
raw = input().split()
d = []
prev = 0
for i in range(n):
    di = int(raw[i])
    di += prev
    d.append(di)
    prev = di
i = n - 2
cur = d[n - 1]
while i > 0:
    cur = max(cur, d[i] - cur)
    i -= 1

print(cur)
