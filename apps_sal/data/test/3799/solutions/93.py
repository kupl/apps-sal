S = list(str(input()))
Slen = len(S)
fro = S[0]
bac = S[-1]
if fro == bac:
    if Slen % 2 == 0:
        print('First')
    else:
        print('Second')
elif Slen % 2 == 0:
    print('Second')
else:
    print('First')
