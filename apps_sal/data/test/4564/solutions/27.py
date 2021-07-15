a=[0]*26
S=input()
i=0
while True:
    if i==len(S):
        print("yes")
        break
    b=ord(S[i])-97
    if a[b]==1:
        print("no")
        break
    else:
        a[b]=1
        i+=1
