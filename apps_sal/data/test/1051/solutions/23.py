k = int(input())
a = list(map(int, input().split()))
maxi = 0
for i in range(k):
    maxi = max(maxi, a[i])
print(max(0, maxi - 25))

