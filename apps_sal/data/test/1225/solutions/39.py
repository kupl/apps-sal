H = int(input())

i = 0
while True:
  if H < 2 ** i:
    n = i
    break
  i += 1

print((2**n -1))

