n = int(input())
a = list(map(int, input().split()))
d = 1
m = 0
for i in range(1,n):
    if a[i] >= a[i-1]:
        d += 1
    else:
        m = max(m,d)
        d = 1
m = max(m,d)
print(m)

