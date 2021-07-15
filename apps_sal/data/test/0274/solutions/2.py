N = int(input())
a = input()
spaces = a.count('[]')
a = list(map(lambda x: 1 if x=='[' else -1, [x for x in str(a) if x=='[' or x==']']))
maxdepth = max([sum(a[:i+1]) for i in range(len(a))])

dl = 5+(maxdepth-1)*2
maxdl = dl-2
#for i in a:
jj = [[' ' for i in range(N+spaces*3)] for j in range(maxdl)]
posx = 0
for i in range(len(a)):
    if a[i] == 1:
        dl -= 2
        for j in range((maxdl-dl)//2,maxdl-(maxdl-dl)//2):
                if j in [(maxdl-dl)//2,maxdl-(maxdl-dl)//2-1]:
                    jj[j][posx]='+'
                    jj[j][posx+1]='-'
                else:
                    jj[j][posx]='|'
        if i < len(a) and a[i+1] == -1:
            posx+=4
        else:
            posx+=1
    elif a[i] == -1:
        for j in range((maxdl-dl)//2,maxdl-(maxdl-dl)//2):
                if j in [(maxdl-dl)//2,maxdl-(maxdl-dl)//2-1]:
                    jj[j][posx]='+'
                    jj[j][posx-1]='-'
                else:
                    jj[j][posx]='|'
        dl += 2
        posx+=1
for j in jj:
    for i in j:
        print(i,end='')
    print()

