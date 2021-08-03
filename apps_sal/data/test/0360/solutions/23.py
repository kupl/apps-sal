n = int(input())
a = [0] * 50001
for i in range(n):
    l, r = list(map(int, input().split()))
    for j in range(l, r + 1):
        a[j] = i
k = int(input())
print(n - a[k])
