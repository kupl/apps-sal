n,m,x=map(int, input().split())
a=[int(i) for i in input().split()]

count_1=0
for i in range(x):
    if i in a:
        count_1+=1
        
count_2=0
for i in range(x,n):
    if i in a:
        count_2+=1
        
print(min(count_1, count_2))
