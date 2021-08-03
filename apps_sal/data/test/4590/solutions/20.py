def getval():
    n, m, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a = [A[0]]
    b = [B[0]]
    for i in range(0, n - 1):
        a.append(a[i] + A[i + 1])
    for i in range(0, m - 1):
        b.append(b[i] + B[i + 1])
    return n, m, k, a, b


def main(n, m, k, a, b):
    idxa = 0
    ans = 0
    t = 0
    while a[idxa] <= k and idxa < n:
        idxa += 1
        if idxa == n:
            break
    ans = idxa
    idxa -= 1
    t = a[idxa]
    for i in range(m):
        t = a[idxa] + b[i]
        if t <= k:
            ans = max(ans, idxa + i + 2)
        else:
            flag = False
            while t > k:
                idxa -= 1
                if idxa < 0:
                    a.append(0)
                    break
                t = a[idxa] + b[i]
            ans = max(ans, idxa + i + 2)

    print(ans)


def __starting_point():
    n, m, k, a, b = getval()
    main(n, m, k, a, b)


__starting_point()
