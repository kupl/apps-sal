n=int(input())
l=list(map(int, input().split(' ')))

out=[-1]*n

pas = 0
pos = [0]
out[0]=0

while pos :
    pas+=1
    new_pos=[]
    for p in pos :
        for q in [p-1,p+1,l[p]-1] :
            if q>=0 and q<n and out[q]==-1:
                out[q]=pas
                new_pos.append(q)
    pos = new_pos
    
print(*out)
