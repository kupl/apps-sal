a = list(map(int, input().split()))
a.sort()
print(a[-1] * 10 + a[0] + a[1])
