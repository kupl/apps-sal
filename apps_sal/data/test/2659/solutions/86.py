t = i = 1
k = int(input()) 
while k:
  if t < i / sum(map(int, list(str(i)))):
    i += 9 * t
    t *= 10
  else:
    print(i)
    i += t
    k -= 1
