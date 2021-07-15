T = int(input())

for t in range(T):
    n = int(input())
    S = [int(_) for _ in input().split()]
    setS = set(S)

    for k in range(1, 1025):
        for el in setS:
            if el ^ k not in setS:
                break
        else:
            print(k)
            break
    else:
        print(-1)

