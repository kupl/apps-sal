n = int(input())
a = list(map(int, input().split()))
d = dict()
for i in range(n):
    d[a[i] - i] = 0
maxi = 0
for i in range(n):
    d[a[i] - i] += a[i]
    if d[a[i] - i] > maxi:
        maxi = d[a[i] - i]
print(maxi)
    

