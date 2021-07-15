s=input()
t=input()

s_l=len(s)
t_l=len(t)

ans=[]
for i in range(s_l-t_l+1):
  judge=True

  ts=list(s)
  for j in range(t_l):
    if ts[i+j]==t[j]:
      pass
    elif ts[i+j]=='?':
      ts[i+j]=t[j]
    else:
      judge=False
      break

    if judge and j==t_l-1:
      for k in range(s_l):
        if ts[k]=='?':
          ts[k]='a'
      ans.append(ts)

if ans:
  ans.sort()
  print(''.join(ans[0]))
else:
  print('UNRESTORABLE')
