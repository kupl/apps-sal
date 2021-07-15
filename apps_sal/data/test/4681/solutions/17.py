n = int(input())
luk = [2,1]
for i in range(2,n+1):
    luk.append(luk[i-1]+luk[i-2])
print(luk[-1])
