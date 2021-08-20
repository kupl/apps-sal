import itertools
kostki = []
for i in range(int(input())):
    kostki.append(input().split())
l = [''.join(i) for i in itertools.product(*kostki)]
s = [(1, 2, 3), (1, 2), (1, 3), (2, 3), (1,), (2,), (3,)]
s1 = []
for p in s:
    s1 += itertools.permutations(p)
res = set()
for inp in l:
    for p in s1:
        num = ''
        for ind in p:
            if ind <= len(inp):
                num += inp[ind - 1]
        if num:
            res.add(int(num))
for i in range(1, 1003):
    if i not in res:
        print(i - 1)
        break
