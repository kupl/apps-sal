w = input()
S = 'abcdefghijklmnopqrstuvwxyz'
flag = True
for c in S:
    if w.count(c) % 2 == 1:
        flag = False
if flag:
    print('Yes')
else:
    print('No')
