n, m = list(map(int, input().split()))
a = ''
for _ in range(n):
    a = input()
ans = 0
i = 0
while i < m:
    if 'B' == a[i]:
        ans += 1
        while i < m and 'B' == a[i]:
            i += 1
    else:
        i += 1
print(ans)
