n = int(input())
a = list(map(int, input().split()))
l = [0] * (n + 1)
for i in range(n):
    l[a[i]] = i + 1
for i in range(1, n + 1):
    print(l[i], end=" ")
