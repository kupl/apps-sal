n = int(input())
a = list(map(int, input().split()))
l = [0] * n
for i in range(n - 1):
    l[a[i] - 1] += 1
for i in range(n):
    print(l[i])
