n = int(input())
a = input()

pos = n // 2

ans = -1

for it in range(n // 2, n // 2 - 5, -1):
    while pos >= 0 and a[pos] == '0':
        pos -= 1

    if (pos < 0):
        break

    if pos > 0:
        cur = int(a[0:pos]) + int(a[pos:len(a)])
        if ans == -1:
            ans = cur
        else:
            ans = min(ans, cur)

    pos -= 1

pos = n // 2

for it in range(n // 2, n // 2 + 5):
    while pos < n and a[pos] == '0':
        pos += 1

    if (pos >= n):
        break

    if pos > 0:
        cur = int(a[0:pos]) + int(a[pos:len(a)])
        if ans == -1:
            ans = cur
        else:
            ans = min(ans, cur)

    pos += 1

print(ans)
