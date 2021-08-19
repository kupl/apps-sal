from sys import stdin
n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
q = int(stdin.readline())
lis = [0] * (10 ** 5 + 10)
four = 0
two = 0
for i in a:
    lis[i] += 1
    if lis[i] % 2 == 0:
        two += 1
    if lis[i] % 4 == 0:
        four += 1
for loop in range(q):
    (c, l) = stdin.readline().split()
    l = int(l)
    if c == '+':
        lis[l] += 1
        if lis[l] % 2 == 0:
            two += 1
        if lis[l] % 4 == 0:
            four += 1
    else:
        if lis[l] % 2 == 0:
            two -= 1
        if lis[l] % 4 == 0:
            four -= 1
        lis[l] -= 1
    if four >= 1 and two >= 4:
        print('YES')
    else:
        print('NO')
