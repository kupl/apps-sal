K = int(input())
if K <= 50:
    a = [50]*K + [0]*(50-K)
    print(50)
    print(*a)
    return

d,m = divmod(K,50)
if m==0:
    a = [d+49] * 50
    print(50)
    print(*a)
    return

a = [d+50] * 50
rem = 50 - m
for i in range(m):
    a[i] += rem
for i in range(m,50):
    a[i] -= (m+1)
print(50)
print(*a)
