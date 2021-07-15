s=int(input())

a_list=[s]


a=s
while True:
    
    if a%2==0:
        a=a//2
    else:
        a=3*a+1
    
    if a in a_list:
        break
    else:
        a_list.append(a)

ans=len(a_list)+1

print(ans)
