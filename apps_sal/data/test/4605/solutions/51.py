N,A,B = map(int,input().split())
ans_list = []

for i in range(0,N+1):

    temp = list(map(int,str(i)))
    temp=sum(temp)
    if temp >=A and temp<=B:
        ans_list.append(i)
            
print(sum(ans_list))
