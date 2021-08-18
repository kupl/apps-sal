
for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    a = []
    taken = [False] * (2 * n + 1)
    for bi in b:
        taken[bi] = True

    for bi in b:
        a.append(bi)
        next = bi + 1
        while next <= 2 * n and taken[next]:
            next += 1

        if next <= 2 * n:
            a.append(next)
            taken[next] = 1
        else:
            break

    if len(a) == 2 * n:
        print(' '.join(map(str, a)))
    else:
        print(-1)
