n=int(input())
abc="abcdefghijklmnopqrstuvwxyz"
ans=""
while True:
  if n % 26 == 0:
    ans += "z"
    n = (n-1)//26
  else:
    ans += abc[n%26-1]
    n //= 26
  if n == 0:
    print(ans[::-1])
    break
