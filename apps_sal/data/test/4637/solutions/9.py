for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    n -= 1
    for i in range(k):
        if a[i] < b[n]:
            a[i] = b[n]
            n -= 1
        else:
            break
    print(sum(a))
