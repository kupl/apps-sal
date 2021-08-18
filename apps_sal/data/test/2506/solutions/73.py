n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)

l = [n for i in range(a[0] + 1)]
for i in range(2, n + 1):
    for j in range(a[-i], a[-i + 1], -1):
        l[j] = n - i + 1

start = 2 * a[-1]
stop = 2 * a[0]
while start < stop:
    i = (start + stop + 1) // 2
    num = 0
    for j in a:
        if i - j < 0:
            num += n
        elif i - j <= a[0]:
            num += l[i - j]
        else:
            break

    if num >= m:
        start = i
    else:
        stop = i - 1

num = 0
for i in a:
    if start - i < 0:
        num += n
    elif 0 <= start - i <= a[0]:
        num += l[start - i]
    else:
        break

ans = 0
for i in a:
    if start - i < 0:
        ans += 2 * i * n
    elif start - i <= a[0]:
        ans += 2 * i * l[start - i]
    else:
        break
ans -= (num - m) * start
print(ans)
