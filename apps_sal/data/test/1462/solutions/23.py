n,k=list(map(int,input().split()))
inpt=input()
Main=[0]*26
for count in inpt:
    Main[ord(count)-ord('A')]+=1
Main.sort(reverse=True)
MainPrint=0
for i in range(26):
    if k<=Main[i]:
        MainPrint+=k**2
        break
    else:
        MainPrint+=Main[i]**2
        k-=Main[i]
print(MainPrint)

