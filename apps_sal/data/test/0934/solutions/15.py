c1 = input()
cards = input().split(' ')

for c in cards:
  if c[0] == c1[0] or c[1] == c1[1]:
    print('YES')
    return
print('NO')

