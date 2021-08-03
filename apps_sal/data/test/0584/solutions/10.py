n = input()
s = input() + '_'

inbrackets = False
l = 0
c = 0

length = len(s)

cur = 0
for i in range(length):
    if s[i] == '_':
        if not inbrackets:
            l = max(l, cur)
        else:
            if cur > 0:
                c += 1
        cur = 0
    elif s[i] == '(':
        if not inbrackets:
            l = max(l, cur)
        else:
            if cur > 0:
                c += 1
        inbrackets = True
        cur = 0
    elif s[i] == ')':
        if not inbrackets:
            l = max(l, cur)
        else:
            if cur > 0:
                c += 1
        inbrackets = False
        cur = 0
    else:
        cur += 1

print(l, c)
