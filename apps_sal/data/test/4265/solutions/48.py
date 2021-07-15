S = input()
T = input()
retval = len(S)
for i in range(len(S)):
  if(S[i]==T[i]):
    retval-=1
print(retval)
