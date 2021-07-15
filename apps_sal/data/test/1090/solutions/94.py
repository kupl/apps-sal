n, k = map(int, input().split())
s = input()
g = []
a = 'A'
s = s+'B'
cnt = 1
for i in s:
  if a == i:
    cnt+=1
  else:
    a = i
    g.append(cnt)
    cnt = 1
print(n-max(1,len(g[1:])-2*k))
