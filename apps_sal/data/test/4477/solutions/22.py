for _ in range(int(input())):
    x = int(input())
    a = x
    cnt = 0
    while a != 0:
        a = a // 10
        cnt += 1
    a = x % 10
    ans = (a - 1) * 10 + cnt * (cnt + 1) // 2
    print(ans)
