s = input()
a = 'aeiou'
b = a + 'n'
prev = 'a'
valid = 'YES'
for c in s:
  if prev not in b and c not in a:
    valid = 'NO'
    break
  prev = c
if prev not in b:
  valid = 'NO'
print(valid)

