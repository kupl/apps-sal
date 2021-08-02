for i in ' ' * int(input()):
    n, m = map(int, input().split())
    L = list(map(int, input().split()))
    if n < 3:
        print(-1)
        continue
    if n > m:
        print(-1)
        continue
    else:
        min1 = min(L)
        index1 = L.index(min1)
        LL = L[:]
        LL.pop(index1)
        min2 = min(LL)
        index2 = LL.index(min2)
        if index2 >= index1: index2 += 1
        print(sum(L) * 2 + (m - n) * (min1 + min2))
        for i in range(n):
            if i < n - 1:
                print(i + 1, i + 2)
            else:
                print(1, i + 1)
        for i in range(m - n):
            print(index1 + 1, index2 + 1)
