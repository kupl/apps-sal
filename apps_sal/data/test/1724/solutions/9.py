n = int(input())
a = list(map(int, input().split()))
c = input()
o, k = 0, 0
dp = []
for i in range(n):
    e = int(c[i])
    if(e):
        if(a[i] > k):
            o = o + a[i]
        else:
            o = o + k
            k = a[i]
    k = k + (1 - e) * a[i]
print(o)
