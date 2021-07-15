n = int(input())
s = input()

anw = n

def calc(pos):
  x = s[:pos] + s[:pos]
  if x == s[:pos*2]:
    return 1+n-pos
  return 1e9

for i in range(n):
  anw = min(anw, calc(i))
  
print(anw)
