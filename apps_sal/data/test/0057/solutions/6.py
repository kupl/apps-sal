n = int(input())
xset = set()
yset = set()
for i in range(n):
    x, y = list(map(int, input().split()))
    xset.add(x)
    yset.add(y)
if len(xset) == 2 and len(yset) == 2:
    xset = list(xset)
    yset = list(yset)
    print(abs(xset[0] - xset[1]) * abs(yset[0] - yset[1]))
else:
    print(-1)
