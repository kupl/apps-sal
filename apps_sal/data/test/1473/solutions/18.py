n = int(input())
before, after = {}, {}
for i in range(n):
  a, b = list(map(int, input().split()))
  after[a] = b
  before[b] = a
begin = None
for key in list(after.keys()):
  if key not in before:
    begin = key
    break
sequence = n * [None]
for pos, x in [(0, begin), (1, after[0])]:
  while True:
    sequence[pos] = x
    if x not in after or after[x] == 0:
      break
    x = after[x]
    pos += 2
print(' '.join(map(str, sequence)))

