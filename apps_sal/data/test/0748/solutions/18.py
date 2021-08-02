n = int(input())
a = list(map(int, input().split()))
c = [0] * 8
for i in range(1, 8):
    c[i] = a.count(i)
if c[5] or c[7] or c[1] != n // 3 or c[3] > c[6] or c[4] > c[2] or c[6] - c[3] != c[2] - c[4]:
    print(-1)
else:
    for i in range(c[4]):
        print('1 2 4')
    for i in range(c[2] - c[4]):
        print('1 2 6')
    for i in range(c[3]):
        print('1 3 6')
