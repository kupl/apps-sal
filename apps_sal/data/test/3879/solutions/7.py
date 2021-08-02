def gcd(a, b):
    while(b != 0):
        r = a % b
        a = b
        b = r
    return a


def valid(m, n):
    g = gcd(m, n)
    x = m // g
    y = n // g
    do1 = 0
    tr1 = 0
    do2 = 0
    tr2 = 0
    while(x % 2 == 0):
        x /= 2
        do1 += 1
    while(x % 3 == 0):
        x /= 3
        tr1 += 1

    while(y % 2 == 0):
        y /= 2
        do2 += 1
    while(y % 3 == 0):
        y /= 3
        tr2 += 1

    if(x > 1 or y > 1):
        return -1
    return g * pow(2, max(do1, do2)) * pow(3, max(tr1, tr2))


N = int(input())
A = list(int(i) for i in input().split())
prev = -1
answered = False
for i in range(N):
    if(prev == -1):
        prev = A[i]
        continue
    m = max(A[i], prev)
    n = min(A[i], prev)
    prev = valid(m, n)
    if(prev == -1):
        print("No")
        answered = True
        break
if(not answered):
    print("Yes")
