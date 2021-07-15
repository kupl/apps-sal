s=input()

num=len(s)
ans_list=[]
for i in range(num-2):
    x=int(s[i:i+3])
    ans_list.append(abs(x-753))
    
print((min(ans_list)))

