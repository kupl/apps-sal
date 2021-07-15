n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = 10**19
for k in range(n):
    t = -10**19
    for i in range(n):
        if (i!=k):
            if a[i]>=0:
                t = max(max(b) * a[i], t)
            else:
                t = max(min(b) * a[i], t)
    m = min(t, m)
print(m)

