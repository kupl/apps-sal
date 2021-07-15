inp = input().split()
k = int(inp[0])
a = int(inp[1])
b = int(inp[2])
ans = 0
if (a > b) :
  c = a
  a = b
  b = c
if a > 0 and b > 0 :
  ans = b // k - ((a - 1) // k)
elif a < 0 and b < 0 :
  ans = 0 - (((a - 1) // k) - b // k)
elif a < 0 :
  ans = (0 - a) // k + b // k + 1
else :
  ans = b // k + 1
print (ans)
