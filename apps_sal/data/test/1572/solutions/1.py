n = int(input())
A = list(map(int, input().split()))
if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    MAX_L = 2
    i1 = 0
    i2 = 1
    while i2 < n:
        CUR_L = 2
        while i2 < n - 1 and A[i1] + A[i2] == A[i2 + 1]:
            i1 += 1
            i2 += 1
            CUR_L += 1
        MAX_L = max(MAX_L, CUR_L)
        i1 += 1
        i2 += 1
    print(MAX_L)
