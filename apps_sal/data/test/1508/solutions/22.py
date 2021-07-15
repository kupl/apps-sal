input()
a = sorted(map(int, input().split()))
t = a[-1]
a[-1] = a[0]
a[0] = t
print(*a)
