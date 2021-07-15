n, s = list(map(int, input().split()))
maxi = 0
for i in range(n):
    a, b = list(map(int, input().split()))
    maxi = max(maxi, max(b - (s - a), 0))
print(maxi + s)

