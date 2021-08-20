n = int(input())
l = list(map(int, input().split()))
for i in range(0, n // 2, 2):
    (l[i], l[n - i - 1]) = (l[n - i - 1], l[i])
print(*l)
