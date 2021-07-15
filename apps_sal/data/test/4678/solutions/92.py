n=int(input())
a=list(map(int, input().split()))
max=a[0]
dai=0
for i in range(n):
    #print(f"{i}回目")
    if max>a[i]:
        dai+=max-a[i]
       
    else:
        max=a[i]
    #print(max,dai)
print(dai)
