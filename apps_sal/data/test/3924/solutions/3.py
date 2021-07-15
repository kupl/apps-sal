n, k = map(int, input().split())
l = [*map(int, input().split())]
c = 0
res = 0
for i, e in enumerate(l):
    if (e + c) < k and c > 0:
        res += int((e + c) > 0)
        c = 0
    else:
        res += (e + c) // k
        c = (e + c) % k
if c > 0: res += 1
print(res)
