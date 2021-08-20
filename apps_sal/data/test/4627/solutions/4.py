T = int(input())
for t in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    par = [a % 2 for a in A]
    odd = sum(par)
    even = N - odd
    res = 'NO'
    if even % 2 == 0 and odd % 2 == 0:
        res = 'YES'
    elif even % 2 != 0 and odd % 2 != 0:
        sA = sorted(A)
        for i in range(N - 1):
            ai = sA[i]
            aip = sA[i + 1]
            if aip - ai == 1:
                res = 'YES'
                break
    print(res)
