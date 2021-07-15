s=input()
np=0
ng=0
ans=0
for si in s:
  if si=='g' and np<ng:
    ans+=1
    np+=1
  elif si=='g' and np>=ng:
    ng+=1
  elif si=='p' and np<ng:
    np+=1
  elif si=='p' and np>=ng:
    ans-=1
    ng+=1
print(ans)
