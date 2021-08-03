from sys import stdin as s
for i in range(int(s.readline())):
    n = int(s.readline())
    l = sorted([i for i in set(map(int, s.readline().split())) if i % 2 == 0], reverse=True)
    t = set()
    c = 0
    for i in l:
        if i not in t:
            t.add(i)
            while i % 2 == 0:
                i //= 2
                t.add(i)
                c += 1
    print(c)
