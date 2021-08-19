N = int(input())
S = input()
i = 0
hidari = str()
migi = str()
a = 0
while i < N:
    if S[i] == ')':
        hidari += '('
        i += 1
    else:
        break
while i < N:
    if S[i] == '(':
        a += 1
    else:
        a -= 1
    i += 1
if a < 0:
    hidari += abs(a) * '('
elif a > 0:
    migi += a * ')'
s = hidari + S + migi
i = 0
hidari = str()
migi = str()
a = 0
while i < N:
    if S[i] == ')':
        hidari += '('
        i += 1
    else:
        break
while i < N:
    if S[i] == '(':
        if a < 0:
            a = 0
        a += 1
        mina = 0
    else:
        a -= 1
        if a < 0:
            if mina > a:
                hidari += '('
    i += 1
if a > 0:
    migi += a * ')'
t = hidari + S + migi
if len(s) == len(t):
    print(s)
elif len(s) > len(t):
    print(s)
else:
    print(t)
