N=input()
#Nのi文字目とi＋1文字目が同じであればカウントを増やす。
j_count=0
for i in range(0,3):
    if N[i]==N[i+1]:
        j_count+=1
if j_count>=2 and N[1]==N[2]:
    print("Yes")
else:
    print("No")

