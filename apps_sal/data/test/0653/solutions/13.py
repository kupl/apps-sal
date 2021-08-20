n = int(input())
s = input()
a = [0 for i in range(10)]
for i in range(n):
    if s[i] == 'L':
        i = 0
        while i < len(a) and a[i] == 1:
            i += 1
        a[i] = 1
    elif s[i] == 'R':
        i = len(a) - 1
        while i > -1 and a[i] == 1:
            i -= 1
        a[i] = 1
    else:
        a[int(s[i])] = 0
print(*a, sep='')
