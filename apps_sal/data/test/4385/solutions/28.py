a=[]
for i in range(6):
    temp=int(input())
    a.append(temp)
for i in range(4):
    for j in range(1,5):
        if a[j]-a[i]>a[5]:
            print(':(')
            return
print('Yay!')
