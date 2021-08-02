import bisect
t = int(input())
for you in range(t):
    l = input().split()
    n = int(l[0])
    k = int(l[1])
    lfi = []
    i = 1
    maxa = 1
    while(i * i <= n):
        if(n % i == 0):
            lfi.append(i)
            if(i > maxa and i <= k):
                maxa = i
            if(i != n // i):
                lfi.append(n // i)
                if(n // i > maxa and n // i <= k):
                    maxa = n // i
        i += 1
    print(n // maxa)
