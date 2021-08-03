input()
a, b = list(map(int, input().split())), list(map(int, input().split()))
am, bm = min(a), min(b)
m = 10
for x in a:
    if x in b:
        if x < m:
            m = x
if m == 10:
    print(min(am, bm), max(am, bm), sep='')
else:
    print(m)
