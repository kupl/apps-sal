a_list=[int(input()) for i in range(5)]

sum=0
for i in a_list:
    #print(((i+9)//10)*10)
    sum+=((i+9)//10)*10

ans_list=[]
for i in a_list:
    b=((i+9)//10)*10-i
    ans_list.append(sum-b)
    
print(min(ans_list))
