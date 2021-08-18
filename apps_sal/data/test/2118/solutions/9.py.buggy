
def arr(n, k, l):
    nonlocal flag
    # print(n,k,l)

    if k == 0:
        return(list(range(l, l + n)))

    if n == 1:
        flag = True
        return([0])

    if (k % 4 == 2):
        k1 = k2 = k // 2 - 1
    else:
        k1 = (k - 4) // 2
        k2 = k1 + 2

    n1 = n // 2
    n2 = n - n1

    a1 = arr(n1, k1, l + n2)
    a2 = arr(n2, k2, l)

    a1.extend(a2)
    return(a1)


n, k = [int(i) for i in input().split()]

flag = False

ans = arr(n, k - 1, 1)

if (k % 2 == 0):
    flag = True

if flag:
    print(-1)
else:
    for i in ans:
        print(i, end=" ")
