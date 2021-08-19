n, m = map(int, input().split())
a = list(map(int, input().split()))
d = {}
for i in a:
    try:
        d[i] += 1
    except KeyError:
        d[i] = 1

# print(d)

mx = m // n

while mx != 0:
    cur = 0
    for i in d:
        t = d[i] // mx
        cur += t
    if cur >= n:
        break
    else:
        mx -= 1

print(mx)
