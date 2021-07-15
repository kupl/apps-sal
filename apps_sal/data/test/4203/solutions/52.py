# 入力
S=input()

# 先頭の文字が 'A'
if S[0]!='A':
  print('WA')
  return

# 先頭から3文字目と末尾から2文字目の間に
# 'C' が含まれる
if 'C' not in S[2:-1]:
  print('WA')
  return

# 上記2文字以外はすべて小文字である
s=list(S)
s.remove('A')
s.remove('C')

for x in s:
  if x not in 'abcdefghijklmnopqrstuvwxyz':
    print('WA')
    return

# チェックに一度もかからなかった場合
print('AC')
