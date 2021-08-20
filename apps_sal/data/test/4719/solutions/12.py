from collections import Counter
n = int(input())
s = [input() for _ in range(n)]
ls = [chr(i) for i in range(ord('a'), ord('z') + 1)]
li = [9999 for _ in range(ord('a'), ord('z') + 1)]
c = []
for x in s:
    c.append(Counter(x))
for x in c:
    for (i, y) in enumerate(ls):
        li[i] = min(x[y], li[i])
res = ''
for (i, x) in enumerate(li):
    res += ls[i] * x
print(res)
