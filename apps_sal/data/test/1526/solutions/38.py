abc = sorted(list(map(int, input().split())))
a, b, c = abc[0], abc[1], abc[2]
res = (c - b)
a += res
if (c - a) % 2:
    print(res + (c + 1 - a) // 2 + 1)
else:
    print(res + (c - a) // 2)
