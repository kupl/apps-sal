N = int(input())
temp = []
for i in range(1,N+1):
    if (i%3 ==0)or(i%5==0)or((i%3==0)&(i%5==0)):
        pass
    else:
        temp.append(i)
print(sum(temp))
