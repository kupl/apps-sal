a = list(map(int, input().split()))
a.sort()
a[2] -= 1
ans = (a[2] - a[1] > 0) * (a[2] - a[1]) + (a[2] - a[0] > 0) * (a[2] - a[0])
print(ans)
