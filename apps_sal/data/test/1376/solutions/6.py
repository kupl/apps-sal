n = int(input())
l = [*map(int, input().split())]
s = set()
l1, l2 = [], []
for i, e in enumerate(l):
    if e in s:
        l2.append((e, i))
    else:
        l1.append((e, i))
        s.add(e)

l1.sort()
l2.sort()

res = 0

prev = 0
for e, i in l1:
    res += abs(i - prev)
    prev = i
prev = 0
for e, i in l2:
    res += abs(i - prev)
    prev = i

print(res)
