N = int(input())

f = N
while True:
  x = str(f)
  if all(x[i] == x[0] for i in range(len(x))):
    print(x)
    return
  else:
    f += 1
