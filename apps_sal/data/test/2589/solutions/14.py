for _ in range(int(input())):
    (a, b) = map(int, input().split())
    r = list(map(int, input().split()))
    p = sum(r)
    q = p
    if p % b != 0:
        print(a)
    else:
        z = 0
        for i in range(1, a + 1, 1):
            p -= r[i - 1]
            q -= r[-i]
            if p % b != 0:
                print(a - i)
                z = 1
                break
            elif q % b != 0:
                print(a - i)
                z = 1
                break
        if z == 0:
            print(-1)
