from math import ceil
s = input()
(x, y) = list(map(int, input().split()))
s2 = s.split('T')
N = len(s2)
dp_x = [set() for i in range(ceil(N / 2) + 1)]
dp_x[0].add(0)
dp_y = [set() for i in range(N // 2 + 1)]
dp_y[0].add(0)
for k in range(N):
    c = len(s2[k])
    if k == 0:
        for a in dp_x[0]:
            dp_x[1].add(a + c)
    elif k % 2 == 1:
        for b in dp_y[(k - 1) // 2]:
            dp_y[(k + 1) // 2].add(b + c)
            dp_y[(k + 1) // 2].add(b - c)
    elif k % 2 == 0:
        for a in dp_x[k // 2]:
            dp_x[(k + 2) // 2].add(a + c)
            dp_x[(k + 2) // 2].add(a - c)
if x in dp_x[-1] and y in dp_y[-1]:
    print('Yes')
else:
    print('No')
