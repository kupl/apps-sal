S = input()
T = ''
SS = S[::-1]
d = 'maerd'
dd = 'remaerd'
e = 'esare'
ee = 'resare'
cnt1 = 0
cnt2 = 5
for i in range(4, len(S)):
    if SS[cnt1:cnt2] == dd:
        T += dd
        cnt1 = cnt2
        cnt2 += 1
    elif SS[cnt1:cnt2] == ee:
        T += ee
        cnt1 = cnt2
        cnt2 += 1
    elif SS[cnt1:cnt2] == d:
        T += d
        cnt1 = cnt2
        cnt2 += 1
    elif SS[cnt1:cnt2] == e:
        T += e
        cnt1 = cnt2
        cnt2 += 1
    else:
        cnt2 += 1
print('YES' if S == T[::-1] else 'NO')
