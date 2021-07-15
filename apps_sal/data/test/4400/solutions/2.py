S=input()
s=0
t=0
for i in range(len(S)):
    if S[i]=="R":
        s=s+1
        if s>t:
            t=s
    else:
        s=0
print(t)
