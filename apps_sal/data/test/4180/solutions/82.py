n = int(input())

x = 0

while True:
  x += 1
  if n <= x*1000:
    print(x*1000-n)
    return
