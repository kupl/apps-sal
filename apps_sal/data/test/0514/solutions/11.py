import math
for _ in range(int(input())):
    (n, d) = list(map(int, input().split()))
    flag = False
    for i in range(n):
        if i + int(math.ceil(d / (i + 1))) <= n:
            flag = True
            break
    if flag:
        print('YES')
    else:
        print('NO')
