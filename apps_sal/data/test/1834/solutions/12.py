n = int(input())
a = list(map(int, input().split()))
a.sort()
l = 0
k = (n + 1) // 2
for i in range((n + 1) // 2):
    print(a[l], end=' ')
    if k < n:
        print(a[k], end=' ')
    l += 1
    k += 1
