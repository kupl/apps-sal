n=int(input())

march=[0]*5

march_dic={"M":0,"A":1,"R":2,"C":3,"H":4}

for i in range(n):
    name=input()
    if name[0] in "MARCH":
        march[march_dic[name[0]]]+=1

def count_type(march):
    ans=[]
    for i in march:
        if i!=0:
            ans.append(i)
    ans.sort()
    return len(ans),ans

type_num,each_num=count_type(march)
if type_num<3:
    print((0))
else:
    ans=0
    for i in range(type_num-2):
        for j in range(i+1,type_num-1):
            for k in range(j+1,type_num):
                ans+=each_num[i]*each_num[j]*each_num[k]

    print(ans)

