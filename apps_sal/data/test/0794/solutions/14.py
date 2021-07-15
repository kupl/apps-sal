n = int(input())
a = [int(i) for i in input().split()]
a.sort()
if a[0] == a[-1]:
    print(-1)
else:
    print(*a)
