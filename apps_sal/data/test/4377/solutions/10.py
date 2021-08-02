a = list(map(int, input().split()))
a.sort()
for i in a[:-1]:
    print(a[-1] - i, end=" ")
