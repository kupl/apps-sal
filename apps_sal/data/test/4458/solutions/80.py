n = int(input())
p = list(map(int, input().split()))
mi = p[0]
res = 0
for v in p:
    mi = min(v, mi)
    if mi == v:
        res += 1
print(res)
