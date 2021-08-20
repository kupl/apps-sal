n = int(input())
s = input()
t = len(s)
a = [0] * (n + 10)
cur = 0
for i in s:
    if i == 'U' and cur != 0 and (a[cur - 1] == 'R'):
        cur -= 1
        t -= 1
        a[cur] = 'D'
        cur += 1
    elif i == 'R' and cur != 0 and (a[cur - 1] == 'U'):
        cur -= 1
        t -= 1
        a[cur] = 'D'
        cur += 1
    elif i == 'U' or i == 'R':
        a[cur] = i
        cur += 1
print(t)
