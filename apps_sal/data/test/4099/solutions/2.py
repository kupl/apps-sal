N, K, M = list(map(int, input().split()))
A1 = list(map(int, input().split()))
add=[]
for i in range(0,K+1):
    if (sum(A1)+i)//N >=M:
        add.append(i)
    else:
        pass

if not add:
    print((-1))
elif K>max(add):
    print((-1))
else:
    print((min(add)))


