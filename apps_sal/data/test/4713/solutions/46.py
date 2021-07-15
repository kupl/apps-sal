N=int(input())
S=input()
a=[]
total=0
for i in range(len(S)):
    if S[i]=="I":
        total+=1
        a.append(total)
    else:
        total-=1
        a.append(total)
print(max(max(a),0))
