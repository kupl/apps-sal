x = int(input())

def isprime(s):
  if s>2 and s%2==0:
    return False
  else:
    flg = True
    for i in range(3, s//2+1, 2):
      if s%i == 0:
        flg = False
        break
    return flg

for i in range(x, 10**6):
  if isprime(i) == True:
    print(i)
    break
