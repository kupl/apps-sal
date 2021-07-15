n=int(input())

for i in range(1,40):
    for j in range(1,40):
        #print(i,j)
        if 3**i+5**j==n:
            print(i,j)
            return
print(-1)
