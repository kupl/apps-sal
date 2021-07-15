N=int(input())
info=[]
for i in range(N):
  info.append(list(map(int,input().split())))
info=list(filter(lambda x:x[2]!=0,info))
xy_00=max(map(lambda x:x[2]-(x[0]+x[1]),info))
xy_10=max(map(lambda x:x[2]-((100-x[0])+x[1]),info))
xy_01=max(map(lambda x:x[2]-(x[0]+(100-x[1])),info))
xy_11=max(map(lambda x:x[2]-((100-x[0])+(100-x[1])),info))

cx1=(-xy_00+xy_10+100)//2
cx2=(-xy_01+xy_11+100)//2
cy1=(-xy_00+xy_01+100)//2
cy2=(-xy_10+xy_11+100)//2
flag=False
for cx in [cx1,cx2]:
  for cy in [cy1,cy2]:
    ch=info[0][2]+(abs(info[0][0]-cx)+abs(info[0][1]-cy))
    for i in info:
      if not ch==i[2]+abs(cx-i[0])+abs(cy-i[1]):
        break
    else:
      print(f"{cx} {cy} {ch}")
      flag=True
      break
  if flag==True:
    break
