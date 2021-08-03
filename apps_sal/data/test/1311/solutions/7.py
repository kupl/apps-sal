from pip._vendor.distlib.compat import raw_input

n = int(input())
a = []

for i in range(n):
    ta, tb = list(map(int, input().split()))
    a.append((ta, tb))

a.sort()
ans = 1
ta, tb = a[0][0], a[0][1]
for i in range(1, n):
    if a[i][0] - a[i][1] >= ta + tb:
        ans += 1
        ta = a[i][0]
        tb = a[i][1]
    elif a[i][0] + a[i][1] < ta + tb:
        ta = a[i][0]
        tb = a[i][1]
print(ans)
