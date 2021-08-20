n = int(input())
a = input()
(ans, start) = (a[0], 1)
while start < n:
    if a[start - 1] != a[start]:
        ans += a[start]
    start += 1
print(len(ans))
