n, k = map(int, input().split(' '))
a = input().split(' ')
for i in range(n):
    a[i] = int(a[i])
s = 0.0
for i in range(n-k+1):
    prom = sum(a[i:i+k])
    num = k
    if prom / num > s:
        s = prom /num
    for j in range(i+k, min(n, i+2*k)):
        prom += a[j]
        num += 1
        if prom / num > s:
            s = prom/num
print(s)
