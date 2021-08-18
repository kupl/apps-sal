n, k = map(int, input().split())
s = input()
res = 1

i = -1
j = 0
cur = 0

while i < j <= n:
    if j == n and i == n - 1:
        break

    while cur <= k and j < n:
        if cur == k and s[j] == 'b':
            break
        else:
            cur += (s[j] == 'b')
            j += 1

    res = max(res, j - i - 1)

    if k > 0:
        if cur < k and i < j - 1:
            i += 1
            cur -= (s[i] == 'b')

        while cur == k and i < j - 1:
            i += 1
            cur -= (s[i] == 'b')
    else:
        i = j
        j = i + 1
res = max(res, j - i - 1)

i = -1
j = 0
cur = 0

while i < j <= n:
    if j == n and i == n - 1:
        break

    while cur <= k and j < n:
        if cur == k and s[j] == 'a':
            break
        else:
            cur += (s[j] == 'a')
            j += 1

    res = max(res, j - i - 1)

    if k > 0:
        if cur < k and i < j - 1:
            i += 1
            cur -= (s[i] == 'a')

        while cur == k and i < j - 1:
            i += 1
            cur -= (s[i] == 'a')
    else:
        i = j
        j = i + 1
res = max(res, j - i - 1)


print(res)
