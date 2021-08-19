for _ in range(int(input())):
    n = int(input())
    kek = dict()
    kek[2] = 0
    kek[3] = 0
    i = 2
    while i < 4 and n > 1:
        if n % i == 0:
            n //= i
            kek[i] += 1
        else:
            i += 1
    if n != 1:
        print(-1)
    elif kek[2] > kek[3]:
        print(-1)
    else:
        ans = kek[3]
        ans += kek[3] - kek[2]
        print(ans)
