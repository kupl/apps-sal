n = int(input())
ar = list(map(int, input().split()))
ar.sort()
s = 0
su = sum(ar)
for x in range(n):
    s += ar[x]
    s += su
    su -= ar[x]
print(s - ar[n - 1])
