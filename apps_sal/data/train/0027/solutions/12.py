for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = dict()
    for j in range(n):
        if a[j] % 2 == 0:
            b[a[j]] = b.get(a[j], 0) + 1
    k = 0
    for key in b:
        c = key
        while c % 2 == 0:
            k += 1
            c = c // 2
            if c in b.keys():
                break
    print(k)
