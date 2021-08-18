from sys import stdin, stdout
T = int(stdin.readline().strip())
for caso in range(T):

    a, b = list(map(int, stdin.readline().strip().split()))
    ans = 0
    while a > b:
        if a % 8 == 0 and a // 8 >= b:
            a = a // 8
            ans += 1
        elif a % 4 == 0 and a // 4 >= b:
            a = a // 4
            ans += 1
        elif a % 2 == 0 and a // 2 >= b:
            a = a // 2
            ans += 1
        else:
            break
    while a < b:
        if a * 8 <= b:
            a = a * 8
            ans += 1
        elif a * 4 <= b:
            a = a * 4
            ans += 1
        elif a * 2 <= b:
            a = a * 2
            ans += 1
        else:
            break
    if a == b:
        print(ans)
    else:
        print(-1)
