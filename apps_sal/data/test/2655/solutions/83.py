n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

ans = a[0]
ch = 1

for i in range(1, n):
    if ch == n - 1:
        break
    else:
        ans += a[i]
        ch += 1

    if ch == n - 1:
        break
    else:
        ans += a[i]
        ch += 1

print(ans)
