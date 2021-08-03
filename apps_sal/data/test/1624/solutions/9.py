n = int(input())
a = list(map(int, input().split()))
a.sort()
su = 0
for i in range(n // 2):
    su += ((a[i] + a[n - i - 1])**2)

print(su)
