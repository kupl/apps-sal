S = input()

flg = True
cnt = 0
for i in range(len(S)):
    if i == 0:
        if S[0] != 'A': flg = False
    elif i == 1:
        if S[1].isupper(): flg = False
    elif i == len(S) - 1:
        if S[i].isupper(): flg = False
    else:
        if S[i] == 'C': cnt += 1
        elif S[i].isupper(): flg = False

if cnt != 1: flg = False

print(['WA', 'AC'][flg])
