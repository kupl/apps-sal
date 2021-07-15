# https://codeforces.com/problemset/problem/353/D
s    = [0 if x=='M' else 1 for x in input()]
ans  =  0
pre  =  -1
num1 =  0

flg=False
for i in range(len(s)-1, -1, -1):
    if s[i]==1:
        flg=True
        num1+=1
    else:
        if flg==True:
            pre=pre+1
        ans=max(num1, pre)
        pre=ans
print(ans)        
