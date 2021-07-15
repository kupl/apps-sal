n, q = map(int, input().split())
s = input()
ss = [0]*n
cnt = 0

for i in range(n-1):
  if s[i] == 'A' and s[i+1] == 'C':
    cnt +=1    
    ss[i+1] += cnt    
  else:
    ss[i+1] = ss[i]

for i in range(q):
  l, r = map(int, input().split())
  print(ss[r-1]-ss[l-1])
