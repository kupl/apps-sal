n = int(input())
s = input()

dd = 0
dr = 0
while len(s) > 1:
    t = ''
    cd = 0
    cr = 0
    for c in s:
        if c == 'D':
            if dd > 0:
                dd -= 1
            else:
                dr += 1
                t += c
                cd += 1
        else:
            if dr > 0:
                dr -= 1
            else:
                dd += 1
                t += c
                cr += 1
    s = t
    if cd == 0:
        s = 'R'
        break
    if cr == 0:
        s = 'D'
        break
    if dd >= cd:
        s = 'R'
        break
    if dr >= cr:
        s = 'D'
        break
    
print(s[0])
