(n, x) = map(int, input().split())
res = []
s = {x}
prev = 0
for i in range(1, 1 << n):
    curr = prev ^ i
    if curr in s:
        continue
    res.append(curr)
    prev = i
    s.add(x ^ i)
print(len(res))
print(*res)
