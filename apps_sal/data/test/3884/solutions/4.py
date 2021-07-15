i=input
i()
m=int(i())
v=m
try:
 for a in map(int, (i()+' '+i()).split()):v*=a/(a-1)
 print(v-m)
except:
 print(-1)
