a, b = list(map(int, input().split()))

diff = b - a

x = 1
y = 3
i = 3

while True:
  if y - x == diff:
    break
  
  x = y
  y = y + i
  i = i + 1

print(y - b)
