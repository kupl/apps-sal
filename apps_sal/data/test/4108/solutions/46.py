S = input()
T = input()
convert = dict()
flg = True
for (s, t) in zip(S, T):
    if s in convert and convert[s] != t:
        flg = False
        break
    convert[s] = t
after = list(convert.values())
if len(after) != len(set(after)):
    flg = False
if flg:
    print('Yes')
else:
    print('No')
