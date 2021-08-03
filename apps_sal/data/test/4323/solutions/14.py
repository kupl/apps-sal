n, m = list(map(int, input().split()))
sumb = 0
suma = 0
s = []
sumschat = 0
k = 0
for i in range(n):
    a, b = list(map(int, input().split()))
    s.append(a - b)
    sumb = sumb + b
    suma = suma + a
if sumb > m:
    print(-1)
else:
    i = 0
    s.sort(reverse=True)
    while sumschat < suma - m:
        sumschat = sumschat + s[i]
        i = i + 1
        k = k + 1
    print(k)
