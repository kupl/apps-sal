t = int(input())
for i in range(t):
 inp = str(input()).split()
 a = int(inp[0])
 b = int(inp[1])
 c = int(inp[2])
 d = int(inp[3])
 count = 0
 count1 = 0
 if a>=d or a>b or c>d:
  pass
 #else:
#   if c<=a:
#       c = a+1
#   if b>=d:
#       b=d-1
 n = d-c+1
 n2 = d-b-1
 c11 = (c-a-1)*n
 c12 = (b-a-1)*n
 c1 = min(c11,c12)
 c2 = n*(n+1)/2 - n2*(n2+1)/2
#   print c2
 c2 = max(c2,0)
 count = c1+c2
 
 n1 = max(d-a,0)
 n2 = max(d-b-1,0)
 n3 = max(c-a-1,0)
 n4 = max(c-b-2,0)
 c1 = n1*(n1+1)/2
 c2 = n2*(n2+1)/2
 c3 = n3*(n3+1)/2
 c4 = n4*(n4+1)/2
 count1 = c1-c2-c3+c4
  
 print(count1)

