import math
t = int(input())
for _ in range(t):
    (n, d) = map(int, input().split())
    if d <= n:
        print('YES')
    else:
        flag = 0
        for i in range(1, min(d, n)):
            if i + math.ceil(d / (i + 1)) <= n:
                print('YES')
                flag = 1
                break
        if flag == 0:
            print('NO')
