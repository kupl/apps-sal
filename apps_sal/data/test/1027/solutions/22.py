a = list(map(int, input().split()))
mx = 0
for i in range(14):
    c = a[i]
    b = a[:]
    b[i] = 0
    res = 0
    for j in range(1, 15):
        b[(i+j)%14] += c//14
        if c%14 >= j:
            b[(i+j)%14] += 1 
        if b[(i+j)%14]%2 == 0:
            res += b[(i+j)%14]
    mx = max(res, mx)
print(mx)

