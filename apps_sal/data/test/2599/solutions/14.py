def cal(a, b, k):
    base = 9*a
    su = (k-b)*(k-b+1)//2 + (k-b+1)
    while (b) :
        su += base
        base -= 1
        b -= 1
    return su

for _ in range(int(input())):
    n, k = map(int, input().split())
    st = ''
    if (n < k*(k+1)//2):
        print(-1)
        continue
    if ((n - k*(k+1)//2) % (k+1) == 0):
        x = (n - k*(k+1)//2)//(k+1)
        st += str(min(x, 9-k))
        x -= min(x, 9-k)
        while (x) :
            st += str(min(9, x))
            x -= min(9, x)
        st = st[::-1]
    for i in range(1, 19):
        for j in range(1, k+1):
            ca = cal(i, j, k)
            if (n < ca) :
                continue
            #print(i, j, ca)
            if ((n-ca) % (k+1)) :
                continue
            t = str(10-j)
            for ii in range(i-1):
                t += '9'
            m = (n-ca) // (k+1)
            if (m):
                t += str(min(8, m))
                m -= min(8, m)
            while (m):
                t += str(min(9, m))
                m -= min(9, m)
            t = t[::-1]
            #print('YES!!!!', i, j, ca)
            if (st) :
                if (int(t) < int(st)):
                    st = t
            else :
                st = t
    if (st) :
        print(st)
    else :
        print(-1)
