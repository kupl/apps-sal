n=int(input())
l = list(map(int,input().split()))
maj = sum(l)//2 + 1
c= [1]
for i in range(1,n):
    if l[i]*2 <= l[0]:
        c.append(i+1)
if sum([l[i-1] for i in c]) >= maj:
    print(len(c))
    print(*c)
else:
    print(0)


