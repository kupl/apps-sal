varianti=[input()[2:] for i in range(4)]
lenz=[len(varianti[i]) for i in range(4)]
counter=0
for i in range(4):
    dub=lenz[:]
    now=dub.pop(i)
    c1=0
    c2=0
    for z in range(3):
        if(now/dub[z]>=2):
            c1+=1
        elif (dub[z]/now>=2):
            c2+=1
    if c1==3 or c2==3 :
        zamechat=i
        counter+=1
if counter==1:
    print(['A','B','C','D'][zamechat])
else:
    print('C')

