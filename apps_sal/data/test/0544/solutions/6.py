def mi():
    return map(int, input().split())


for _ in range(int(input())):
    n = int(input())
    a = list(input())
    flag = 0
    for i in range(n // 2):
        c1 = ord(a[i])
        c2 = ord(a[n - 1 - i])
        if c1 - 1 == c2 - 1 or c1 - 1 == c2 + 1 or c1 + 1 == c2 - 1 or (c1 + 1 == c2 + 1):
            flag = 0
        else:
            flag = 1
            break
    if flag:
        print('NO')
    else:
        print('YES')
