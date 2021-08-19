n = int(input())
a = list(map(int, input().split()))
c = m = 0
for i in range(n):
    if a[i] != 0:
        c += 1
    else:
        m = max(m, c)
        c = 0
m = max(m, c)
print(m)
