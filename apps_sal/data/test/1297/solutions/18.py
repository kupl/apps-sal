n = input()
x = 1
cnt = 0
for i in range(len(n)-1):
    if(n[i] == n[i+1]):
        x+=1
    else:
        if(x % 2 == 0):
            cnt += 1
            x = 1
if(x % 2==0):
    print(cnt+1)
else:
    print(cnt)
    

