n = int(input())
ss = input()
s = ss[::-1]
t = input()[::-1]
tt = [0] * n
for i in range(n):
    c = ord(s[i]) - ord('a')
    tt[i] = ord(t[i]) - ord('a')
    tt[i] -= c
for i in range(n - 1):
    if tt[i] < 0:
        tt[i] += 26
        tt[i + 1] -= 1

tt = tt[::-1]
rem = 0
for i in range(n):
    rem = rem * 26 + tt[i]
    tt[i] = rem // 2
    rem = rem % 2
res = [x for x in ss]
for i in range(n - 1, -1, -1):
    c = tt[i] + ord(res[i]) - ord('a')
    tt[i] = c % 26
    if i > 0:
        tt[i - 1] += c // 26
    res[i] = chr(tt[i] + ord('a'))
print(''.join(res))

