n = int(input())
L = list(map(int, input().split()))
smax = 0
i = 0
j = n - 1
t1 = 0
t3 = 0
t1 += L[i]
t3 += L[j]
while i < j:
    if t1 == t3:
        smax = max(smax, t1)
        i += 1
        t1 += L[i]
    elif t1 > t3:
        j -= 1
        t3 += L[j]
    else:
        i += 1
        t1 += L[i]
print(smax)
