n = input()
s = input()
ss = s
for i in range(50):
  s = s.replace('()','')
l = s.count(')')
r = s.count('(')
print('('*l+ss+')'*r)
