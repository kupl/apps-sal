S = str(input())
s = 'abcdefghijklmnopqrstuvwxyz'

for i in s:
  if i not in S:
    print(i)
    return
print('None')
