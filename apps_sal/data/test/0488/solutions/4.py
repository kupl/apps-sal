s = input()
n = 1

for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        n += 1

mas = [0] * n
col = [0] * n

count = 1
idx = 0
c = s[0]
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        mas[idx] = count
        col[idx] = c
        idx += 1
        count = 1
        c = s[i]

mas[idx] = count
col[idx] = c

res = 0

while n > 1:
    newlen = n
    idx = -1

    for i in range(0, n):
        if (i == 0) or (i == n - 1):
            mas[i] -= 1
        elif mas[i] >= 2:
            mas[i] -= 2
        else:
            mas[i] = 0

        if mas[i] == 0:
            newlen -= 1
        else:
            if idx >= 0 and col[idx] == col[i]:
                mas[idx] += mas[i]
                newlen -= 1
            else:
                idx += 1
                mas[idx] = mas[i]
                col[idx] = col[i]
                type = i % 2

    n = newlen
    res += 1

print(res)
