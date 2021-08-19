from math import inf
t = int(input())
for q in range(t):
    (n, k) = [int(i) for i in input().split()]
    L = [int(i) for i in input().split()]
    F = [0] * 60
    for i in L:
        num = i
        step = 0
        while num:
            F[step] += num % k
            num //= k
            step += 1
    flag = True
    for i in F:
        if i > 1:
            flag = False
            break
    if flag:
        print('YES')
    else:
        print('NO')
