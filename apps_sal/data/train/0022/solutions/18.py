def digits(n):
    l = []
    while(n > 0):
        l.append(n % 10)
        n = n // 10
    mina = min(l)
    maxa = max(l)
    return mina * maxa


t = int(input())
for you in range(t):
    l = input().split()
    a = int(l[0])
    k = int(l[1])
    for i in range(k - 1):
        if(digits(a) == 0):
            break
        a += digits(a)
    print(a)
