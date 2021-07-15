I = lambda: list(map(int, input().split()))

t, = I()
while t:
    t -= 1
    n, = I()
    l = I()
    l = [i-1 for i in l]
    p = [i for i in range(n)]
    v = [0]*n
    for i in range(n):
        if not v[i]:
            v[i] = 1
            j = l[i]
            while not v[j]:
                v[j] = 1
                v[i] += 1
                p[j] = i
                j = l[j]
                
    #print(v)
    for i in range(n):
        print(v[p[i]], end = ' ')
    print()

