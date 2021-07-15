N,K = map (int, input ().split ())
l = [int (x) for x in input().split()]
list.sort (l)
x = 0
for i in range (K):
  x += l[-i-1]
print (x)
