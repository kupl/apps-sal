n, p = map(int, input().split())
if n == 0:
    print(0)
else:
    if p >= n:
        print(-1)
    else:
        i = 0
        while 1:
            n -= p
            if n <= 0:
                print(-1)
                break
            i += 1
            s = str(bin(n))
            k = 0
            for j in s:
                if j == '1':
                    k += 1
            if k <= i and n >= i:
                print(i)
                break
