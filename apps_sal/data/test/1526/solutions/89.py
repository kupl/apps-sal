a = list(map(int, input().split()))
a.sort()
total_diff = a[2] - a[0] + (a[2] - a[1])
if total_diff % 2 == 0:
    print(total_diff // 2)
else:
    print(total_diff // 2 + 2)
