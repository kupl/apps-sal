n = int(input());
a = list(map(int, input().split(' ')))
curr = n
s = set()
for x in a:
    s.add(x)

    l = []
    while n in s:
        l.append(n)
        s.remove(n)
        n -= 1

    print(' '.join(list(map(str, l))))
