n = int(input())
S = input()
lc = 0
rc = 0
for s in S:
    if s == '(':
        rc += 1
    else:
        if rc:
            rc -= 1
        else:
            lc += 1
print('(' * lc + S + ')' * rc)
