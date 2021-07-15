n, k = map(int, input().split())
s = input()

s = s + s

def getVic(c):
    if c[0] == c[1]:
        return c[0]
    else:
        if not 'R' in c:
            return 'S'
        elif not 'S' in c:
            return 'P'
        else:
            return 'R'

for i in range(k):
    s_ = ''
    for j in range(int(len(s) / 2)):
        s_ = s_ + getVic(s[j*2:j*2+2])
    s = s_ + s_

print(s[0])
