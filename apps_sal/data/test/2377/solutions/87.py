from bisect import bisect_right
n,h=map(int,input().split())
a=[]
b=[]
for i in range(n):
    a1,b1=map(int,input().split())
    a.append(a1)
    b.append(b1)
a_s=sorted(a, reverse=1)
b_s1=sorted(b)
b_s=sorted(list(b_s1[bisect_right(b_s1,a_s[0]):]),reverse=1)


count=0
sum=0

for j in b_s:
    sum+=j
    count+=1
    if h<=sum:
        print(count)
        break
else:
    if (h-sum)%a_s[0]==0:
        print(count+(h-sum)//a_s[0])
        
    else:
        print(count+1+(h-sum)//a_s[0])
