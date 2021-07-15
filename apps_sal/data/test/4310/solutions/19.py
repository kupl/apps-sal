al = list(map(int,input().split()))
s = []
for i in range(3):
  s.append(abs(al[-i]-al[1-i])+abs(al[1-i]-al[2-i]))
print(min(s))
