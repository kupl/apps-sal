n, k = map(int, input().split())
l = list(map(int, input().split()))
j = 0
L = list(range(1, n + 1))
for i in l:
    k -= 1
    j = (j + i) % n
    if k != 0:
        print(L[j], end=' ')
    else: print(L[j], end='')
    n -= 1

    L.pop(j)
