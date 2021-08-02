for i in range(int(input())):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    m = max(a)
    for i, val in enumerate(a):
        a[i] = m - a[i]
    k -= 1

    if k % 2 == 0:
        print(" ".join(str(num) for num in a))
    else:
        m = max(a)
        print(" ".join(str(m - num) for num in a))
