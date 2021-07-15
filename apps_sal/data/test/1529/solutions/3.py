n= int(input())
ans=[]

for i in range(n):
    s=input()
    s.lower
    if(s[-5:]=="lala." and s[0:5]=="miao."):
        ans.append("OMG>.< I don't know!")
        continue
    elif(s[-5:]=="lala."):
        ans.append("Freda's")
        continue
    elif(s[0:5]=="miao."):
        ans.append("Rainbow's")
        continue
    else:
        ans.append("OMG>.< I don't know!")

for i in range(n):
    print(ans[i])

