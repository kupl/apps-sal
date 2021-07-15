n = int(input())
for i in range(1,10):
  if 2 ** i > n:
    print((2 ** (i - 1)))
    break

