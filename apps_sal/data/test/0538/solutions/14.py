N = input()
L = len(N)

i = 0
while i < L and N[i] == '0':
  i += 1
j = L-1
while j >= 0 and N[j] == '0':
  j -= 1

if i > L-j-1:
  print('NO')
  return

while i < j:
  if N[i] != N[j]:
    print('NO')
    return
  i += 1
  j -= 1

print('YES')

