s = input()
n = len(s)
a = [0] * n
b = 0
for i in range(n):
    if s[i] == 'R':
        b += 1
    elif b:
        a[i - 1] += 0 - - b // 2
        a[i] += b // 2
        b = 0
a[-1] += b

b = 0
for i in range(n - 1, -1, -1):
    if s[i] == 'L':
        b += 1
    elif b:
        a[i] += b // 2
        a[i + 1] += 0 - - b // 2
        b = 0
a[0] += b
print((*a))

