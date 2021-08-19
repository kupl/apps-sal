def inp(s):
    j = 0
    a = []
    for i in range(len(s)):
        if s[i] == ' ':
            a.append(int(s[j:i]))
            j = i + 1
        if i == len(s) - 1:
            a.append(int(s[j:]))
    return a


def chk(a):
    f = 0
    for i in range(len(a)):
        if a[i] != i:
            f = 1
            break
    return f


n = int(input())
s = input()
a = inp(s)
x = a
for i in range(n):
    f = 0
    if chk(a) == 0:
        f = 1
        break
    for i in range(len(a)):
        if i % 2 == 0:
            a[i] = (a[i] - 1) % n
        else:
            a[i] = (a[i] + 1) % n
if f == 1:
    print('Yes')
else:
    print('No')
