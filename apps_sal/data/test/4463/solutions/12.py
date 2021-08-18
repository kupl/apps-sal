s = list(input())
t = list(input())

s = sorted(s)
t = sorted(t, reverse=True)

flag = [0, 0]

if len(s) < len(t):
    for i in range(len(s)):
        if s[i] < t[i]:
            print('Yes')
            break
        elif s[i] > t[i]:
            print('No')
            break
        elif i == len(s) - 1:
            print('Yes')
elif len(s) > len(t):
    for i in range(len(t)):
        if s[i] < t[i]:
            print('Yes')
            break
        elif s[i] > t[i]:
            print('No')
            break
        elif i == len(t) - 1:
            print('No')
elif len(s) == len(t):
    for i in range(len(s)):
        if s[i] < t[i]:
            print('Yes')
            break
        elif s[i] > t[i]:
            print('No')
            break
        elif i == len(s) - 1:
            print('No')
