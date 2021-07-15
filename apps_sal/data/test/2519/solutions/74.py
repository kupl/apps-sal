n,k = list(map(int,input().split()))
p = list(map(int,input().split()))

sample = []
for i in range(1,1001) :
    sample.append((1+i)/2)

kitaichi = []
for i in range(n) :
    kitaichi.append(sample[p[i]-1])

maxkitaichi = 0
sum = 0
for i in range(k) :
    maxkitaichi += kitaichi[i]
    sum += kitaichi[i]

for i in range(1,n-k+1) :
    sum = sum + kitaichi[i+k-1] - kitaichi[i-1]
    if sum >= maxkitaichi :
        maxkitaichi = sum
        
print(maxkitaichi)

