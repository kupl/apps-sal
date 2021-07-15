num = input().split()
hei = int(num[0])
wei = int(num[1])

photo = []

for i in range(hei):
    temp = input()
    temp = list(temp)
    photo.append(temp)
    photo.append(temp)
    
for i in range(hei*2):
    for j in range(wei):
        print(photo[i][j],end="")
    print("\n",end="")
