S = list(input())

d = list('dream')
e = list('erase')
er = list('er')
r = list('r')
c = 0

while c < len(S):
    if S[c:c + 5] == d:
        c += 5
        if S[c:c + 5] == e:
            c += 5
            if S[c:c + 1] == r:
                c += 1
        elif S[c:c + 2] == er:
            c += 2
    elif S[c:c + 5] == e:
        c += 5
        if S[c:c + 1] == r:
            c += 1
    else:
        print('NO')
        return
print('YES')
