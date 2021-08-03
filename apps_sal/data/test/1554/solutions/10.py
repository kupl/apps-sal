length = int(input())
gems = input().split()

result = []
s = 0
dist = set()
pend_e = 0
pend_s = 0
for i in range(0, length):
    cur = gems[i]
    if cur not in dist:
        dist.add(cur)
    else:
        if pend_e != 0:
            result.append([pend_s, pend_e])
        pend_e = i + 1
        pend_s = s + 1
        s = i + 1
        dist.clear()

if s != 0 and pend_e != length + 1:
    result.append([pend_s, length])

if len(result) == 0:
    print(-1)
else:
    print(len(result))

for r in result:
    print(r[0], r[1])
