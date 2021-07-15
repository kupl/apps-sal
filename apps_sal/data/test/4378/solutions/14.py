def div_process(s, c):
  sl=list(s)
  for i in range(1, len(sl), 2):
    sl[i]=c
  return "".join(sl)

li=0
ct=0
input();i_s=input()
sp_l=[]
for i in range(1, len(i_s)):
  if not i_s[i]==i_s[i-1]:
    sp_l.append(i_s[li:i])
    li=i
sp_l.append(i_s[li:])

for i in range(len(sp_l)-1):
  sp_l[i]=div_process(sp_l[i], list({'R', 'G', 'B'}-{sp_l[i][0], sp_l[i+1][0]})[0])
sp_l[-1]=div_process(sp_l[-1], list({'R', 'G', 'B'}-{sp_l[-1][0]})[0])

print(sum([int(len(x)/2) for x in sp_l]))
print(''.join(sp_l))

