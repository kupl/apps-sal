n = int(input())
l = list(map(int, input().split()))

mini = min(l)
for i in range(n): l[i] -= mini
res = mini * n
tmp = 0
maxi = 0
for i in range(2 * n):
    if l[i % n] > 0:
        tmp += 1
        if tmp > maxi: maxi = tmp
    else: tmp = 0
    
print(res + maxi)
