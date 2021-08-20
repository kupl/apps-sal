def ok(s1, s2):
    return s1[0] == s2[0] or s1[1] == s2[1]


card = input()
hand = input().split()
flag = False
for c in hand:
    if ok(card, c):
        flag = True
if flag:
    print('YES')
else:
    print('NO')
