N=int(input())
ac=0
wa=0
tle=0
re=0
for _ in range(N):
  s=input()
  if 'AC'==s:
     ac+=1
  elif 'WA'==s:
    wa+=1
  elif 'TLE'==s:
    tle+=1
  elif 'RE'==s:
    re+=1
print('AC','x',ac)
print('WA','x',wa)
print('TLE','x',tle)
print('RE','x',re)
