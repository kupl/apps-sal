3
nm = str(input()).split(' ')
prever = int(nm[0])
posver = 0
pregor = int(nm[1])
posgor = 0
z = 1
while z <= int(nm[0]):
    al = list(str(input()))
    rar = al.count('*')
    if rar != 0:
        if prever > z:
            prever = z
        if posver < z:
            posver = z
    x = 0
    while x <= len(al) - 1:
        if al[x] == '*':
            if pregor > x:
                pregor = x
            if posgor < x:
                posgor = x
        x += 1
    z += 1
s1 = abs(pregor - posgor) + 1
s2 = abs(prever - posver) + 1
if s1 >= s2:
    s2 = s1
elif s2 > s1:
    s1 = s2
print(s1)
