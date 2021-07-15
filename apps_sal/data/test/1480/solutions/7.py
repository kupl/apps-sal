n, k = map(int, input().split())
a = list(map(int, input().split()))
cur = 0
x = []
for i in range(n):
    x.append(i + 1)
for i in range(k):
    v = cur
    f = a[i] % n
    for j in range(f):
        v += 1
        if v >= n:
            v = v - n
    
    print(x[v], end=' ')
    x.pop(v)
    n -= 1
    cur = v % n

    
    
