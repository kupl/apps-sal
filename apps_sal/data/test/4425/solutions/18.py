n,k = map(int,input().split())

num = 0

for i in range(1,n+1):
    j = 0
    while True:
        if i*(2**j) >=k:
            break
        j +=1
    
    
    num += 1/(n*(2**j))

print(num)
