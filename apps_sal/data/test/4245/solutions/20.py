a, b = list(map(int, input().split()))

for i in range(1, 21):
  if b == 1:
    i=0
    break
  x = a*i
  x = x - i+1
  if x >= b:
    break

print(i)

