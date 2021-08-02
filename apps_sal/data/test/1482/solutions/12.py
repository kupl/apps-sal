n, m = map(int, input().split())
a = list(map(int, input().split()))
o = []
for i in range(n * m):
    o.append(0)
for i in range(m):
    o[a[i] - 1] = i + 1
for i in range(m):
    for j in range(n - 1):
        for k in range(n * m):
            if(o[k] == 0):
                print(k + 1, end=' ')
                o[k] = i + 1
                break
    print(a[i], end='\n')
