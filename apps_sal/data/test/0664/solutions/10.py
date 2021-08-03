n = int(input())
a = list(map(int, input().split()))
k = 0
for i in range(n - 1):
    if a[i] > a[i + 1]:
        k += 1
if k == 0:
    print(0)
elif k > 1 or a[n - 1] > a[0]:
    print(-1)
else:
    for i in range(n):
        if a[i] > a[i + 1]:
            print(n - i - 1)
            break
