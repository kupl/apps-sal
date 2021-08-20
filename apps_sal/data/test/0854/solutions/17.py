(n, t) = list(map(int, input().split()))
A = list(map(int, input().split()))
ans = 0
while t > 0:
    k = 0
    suma = 0
    t1 = t
    f = 0
    for i in range(n):
        if A[i] <= t1:
            suma += A[i]
            t1 -= A[i]
            k += 1
            f = 1
    if f == 1:
        ans = ans + k * (t // suma)
        t = t % suma
    else:
        break
print(ans)
