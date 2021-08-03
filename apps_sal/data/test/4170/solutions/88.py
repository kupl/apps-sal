input()
count, start, ans, a = 0, 0, 0, [*map(int, input().split())]
while start < len(a) - 1:
    if a[start] >= a[start + 1]:
        count += 1
    else:
        ans = max(ans, count)
        count = 0
    start += 1
print(max(ans, count))
