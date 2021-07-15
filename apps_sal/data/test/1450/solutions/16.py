s = input()
n = len(s)
_0, _1, i = 0, 0, 0
while i < n and s[i] != '2':
  if s[i] == '0': _0 += 1
  elif s[i] == '1': _1 += 1
  i += 1
front = '0'*_0 + '1' * _1
end = ''
for c in s[i:]:
  if c == '1':
    front += c
  else:
    end += c
print(front + end)

