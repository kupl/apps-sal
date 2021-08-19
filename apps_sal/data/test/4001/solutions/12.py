n = int(input())
a = list(map(int, input().split()))
a.sort()
maxi = a[n - 1]
for i in range(1, maxi + 1, 1):
    if maxi % i == 0:
        a.remove(i)
m2 = max(a)
print(maxi, m2)
