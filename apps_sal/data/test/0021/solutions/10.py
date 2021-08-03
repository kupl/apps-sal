n = int(input())
l = 0
r = 0
a = list(map(int, input().split()))
for i in range(n):
    if a[i] == 1:
        l = i + 1
    elif a[i] == n:
        r = i + 1
print(max(l - 1, r - 1, n - l, n - r))
