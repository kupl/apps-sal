n = int(input())
A = list(map(int, input().split()))
inf = 1000000000000
inf = 1000000000000
max1 = -inf
max2 = -inf
max3 = -inf
max1c = 0
max2c = 0
max3c = 0
for q in range(n):
    if A[q] > max1:
        max3 = max2
        max2 = max1
        max1 = A[q]
    elif A[q] > max2 and A[q] < max1:
        max3 = max2
        max2 = A[q]
    elif A[q] > max3 and A[q] < max1 and (A[q] < max2):
        max3 = A[q]
if max2 == max1 - 2:
    max3 = max2
    max2 = -inf
for q in range(n):
    a = A[q]
    if a == max1:
        max1c += 1
    elif a == max2:
        max2c += 1
    else:
        max3c += 1
if max3 != -inf:
    izm1 = min(max1c, max3c) * 2
    izm2 = max2c // 2 * 2
    if izm1 > izm2:
        cnt = 0
        q = 0
        while cnt < izm1 // 2:
            if A[q] == max1:
                A[q] -= 1
                cnt += 1
            q += 1
        cnt = 0
        q = 0
        while cnt < izm1 // 2:
            if A[q] == max3:
                A[q] += 1
                cnt += 1
            q += 1
    else:
        cnt = 0
        q = 0
        while cnt < izm2 // 2:
            if A[q] == max2:
                A[q] -= 1
                cnt += 1
            q += 1
        while cnt < izm2:
            if A[q] == max2:
                A[q] += 1
                cnt += 1
            q += 1
    print(n - max(izm1, izm2))
    print(*A)
else:
    print(n)
    print(*A)
