N=int(input())

for i in range(26):
    for j in range(15):
        if 4*i+7*j==N:
            print("Yes")
            return
           
            
print("No")
