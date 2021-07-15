array = list(map(int,input().split()))
K = array[0]
S = array[1]
count = 0
for i in range(K+1):
    for j in range(K+1):
        z = S - i - j
        if(z >= 0 and z <= K):
            count+=1
print(count)
