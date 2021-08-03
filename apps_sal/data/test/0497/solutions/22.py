n = int(input())
a = list(map(int, input().split()))
if a[0] != a[-1]:
    print(n - 1)
else:
    for i in range(len(a)):
        if a[i] != a[0]:
            l = i
            break
    for i in range(len(a)):
        if a[i] != a[0]:
            r = i
    print(max(r, n - l - 1))
