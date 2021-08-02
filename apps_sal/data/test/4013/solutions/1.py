n = int(input())
a = list(map(int, input().split()))
a.sort()
if a[1] - a[0] >= a[-1] - a[-2]:
    print(a[-1] - a[1])
else:
    print(a[-2] - a[0])
