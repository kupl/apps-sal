c = [0] * 8
n = int(input())
for x in input().split():
    c[int(x)] += 1
if c[5] > 0 or c[7] > 0 or c[1] != c[2] + c[3] or c[1] != c[4] + c[6] or c[4] > c[2]:
    print(-1)
else:
    for i in range(c[4]):
        print('1 2 4')
    for i in range(c[2] - c[4]):
        print('1 2 6')
    for i in range(c[3]):
        print('1 3 6')
