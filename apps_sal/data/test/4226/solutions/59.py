X, Y = map(int, input().split())
count = 0

r = range(2*X, 4*X+2, 2)

for i in r:

  if i == Y:
    count += 1

print('Yes' if count > 0 else 'No')
