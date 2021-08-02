n = int(input())
a = list(map(int, input().split()))
m = -1
for i in range(n):
    if a[i] > m + 1:
        print(i + 1); return
    else:
        m = max(a[i], m)
print(-1)
