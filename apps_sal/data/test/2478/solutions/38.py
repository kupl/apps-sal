N = input()
S = input()
s = S
for i in range(50):
  S = S.replace('()','')
l = S.count(')')
r = S.count('(')
print('('*l+s+')'*r)
