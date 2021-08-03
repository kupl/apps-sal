S = input()
T = input()

convert = dict()

# 変換元の重複チェック？
flg = True
for s, t in zip(S, T):
    if s in convert and convert[s] != t:
        flg = False
        break
    convert[s] = t

# 変換先の重複チェック
after = list(convert.values())
if len(after) != len(set(after)):
    flg = False

if flg:
    print('Yes')
else:
    print('No')
