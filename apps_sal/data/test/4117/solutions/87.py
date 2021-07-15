import itertools
N=int(input())
a=list(map(int, input().split()))
a_=list(itertools.combinations(a,3))
count=0
for i in a_:
  if(len(set(i)) == 3):
    if(i[0]+i[1]>i[2] and i[0]+i[2]>i[1] and i[1]+i[2]>i[0]):
      count=count+1
print (count)
