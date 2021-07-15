n = int(input())
s = set()
x = [1 , 5 , 10 , 50]
l = list()

def dfs(a , b , c):
  if a == n :
    s.add(b)
    return 
  while c < len(x) :
    dfs(a + 1 , b + x[c] , c)
    c += 1


if n <= 10 :
  dfs(0 , 0 , 0)
  print(len(s))
  return
else :
  print(244  + 49 * (n - 10) - 1)  


                                               


