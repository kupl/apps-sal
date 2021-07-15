ls=[]
for i in range(5):
  ls.append(int(input()))
rm=10
time=0
for i in ls:
  if i%10==0:
    time+=i
  else:
    time+=(i//10+1)*10
    rm=min(rm,i%10)
time+=rm-10
print(time)

