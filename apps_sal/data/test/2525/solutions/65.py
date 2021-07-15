S = input()
Q = int(input())
pre = ''#逆順
suf = ''
rev = 0
for i in range(Q):
    inp = input()
    if inp == '1':
        pre, suf = suf, pre
        rev += 1
    else:
        inp_l = inp.split()
        if inp_l[1] == '1':
            pre = pre + inp_l[2]
        else:
            suf = suf + inp_l[2]
if rev%2 == 0:
    print(''.join(list(reversed(pre)))+S+suf)
else:
    print(''.join(list(reversed(pre)))+''.join(list(reversed(S)))+suf)
