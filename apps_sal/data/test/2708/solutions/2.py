j, k = list(map(int, input().split()))
n=j
for i in range(k):
    lastdigit = int(repr(n)[-1])
    if(lastdigit !=0):
        n=n-1
        

    elif(lastdigit ==0):
        n=n//10

print(n)



