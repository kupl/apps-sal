s=input()
a=0
for i in range(len(s)-1):
  if s[i]==s[i+1]:
    print('Bad')
    a=1
    break
if a==0:
    print('Good')
