t = int(input())
for _ in range(t):
    n = int(input())
    d1 = {}
    flag = 0
    for i in range(n):
        s = input()
        for i in s:
            if i not in d1:
                d1[i] = 1
            else:
                d1[i] += 1
    for i in d1:
        if d1[i] % n != 0:
            flag = 1
            break
    if flag == 1:
        print('NO')
    else:
        print('YES')
