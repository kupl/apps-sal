def f(k,L,p): 
  m = L
  while m%3 > 0:
    p += [[k+1,20,(m-1)*(3**k)]]
    m = m-1
  if m == 0:
    print(20,len(p))
    for l in p:
      print(" ".join([str(t) for t in l]))
    return
  for i in range(3):
    p += [[k+1,k+2,i*(3**k)]]
  m = m//3
  if m > 0:
    return f(k+1,m,p)




f(0,int(input()),[])
