a,b,n = map(int, input().split())


if n >= b-1:
  print( (a*(b-1)) // b - a * ((b-1)//b))

else:
  print( (a*n) // b - a * (n//b))
