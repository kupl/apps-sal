n = int(input())
a = list(map(int, input().split()))
l = a[0]
r = a[-1]
k = 0
while (a[k] == a[-1]):
    k += 1


r = 0
while (a[n - r - 1] == a[0]):
    r += 1

print(max(n - k - 1, n - r - 1))
