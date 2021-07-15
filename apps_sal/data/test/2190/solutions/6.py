n, k = list(map(int, input().split()))

a = list(map(int, input().split()))
d = {}
ans = 0

for el in a:
    i = 2
    a = []
    b = []
    while i*i <= el:
        cnt = 0
        while not(el%i):
            el //= i
            cnt += 1
        if cnt%k:
            a.append((i, cnt%k))
            b.append((i, k-(cnt%k)))
        i += 1
    
    if el > 1:
        a.append((el, 1))
        b.append((el, k-1))

    a = tuple(a)
    b = tuple(b)

    ans += d.get(b, 0)
    d[a] = d.get(a, 0)+1
    
print(ans)

