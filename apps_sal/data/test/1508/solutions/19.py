n = int(input())
a = list(map(int, input().split()))
a.sort()
a[0], a[-1] = a[-1], a[0]
for i in a:
    print(i, end=' ')
