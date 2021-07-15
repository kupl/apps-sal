n, m, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
res, i = 1, 0
f = (arr[0] - 1) // k * k + 1
e = f + k - 1
while e < arr[-1]:
    d = 0
    while i + d < m and arr[i+d] <= e: 
        d += 1
    i += d
    if d > 0: 
        e += d
        res += 1
    else:
        f = e + 1
        f += (arr[i] - f) // k * k
        e = f + k - 1
print(res)

