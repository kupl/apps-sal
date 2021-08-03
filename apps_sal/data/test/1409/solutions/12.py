def read():
    return map(int, input().split())


n, k = read()
a = list(read())
a.sort()
i = 0
ans = 0
while i + 2 < len(a):
    if a[i] + k <= 5 and a[i + 1] + k <= 5 and a[i + 2] + k <= 5:
        ans += 1
        i += 3
    else:
        i += 1
print(ans)
