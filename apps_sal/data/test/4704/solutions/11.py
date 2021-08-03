N = int(input())
a = list(map(int, input().split()))
s = sum(a)
su = a[0]
ar = s - su
ans = abs(su - ar)
for i in range(1, N - 1):
    su += a[i]
    ar = s - su
    if ans > abs(su - ar):
        ans = abs(su - ar)
print(ans)
