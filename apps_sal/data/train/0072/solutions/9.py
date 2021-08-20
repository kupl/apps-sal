def beauty(n, k, array):
    s = set(array)
    if len(s) > k:
        print(-1)
        return
    L = list(s)
    L.extend([array[0]] * (k - len(s)))
    L *= n
    print(len(L))
    print(*L)


t = int(input())
for i in range(t):
    (n, k) = list(map(int, input().split()))
    array = list(map(int, input().split()))
    beauty(n, k, array)
