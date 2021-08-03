n = int(input())
flag = False

for i in range(int(n / 4 + 1)):
    for j in range(int(n / 7 + 1)):
        if(flag == False):
            if(i * 4 + j * 7 == n):
                print("Yes")
                flag = True

if(flag == False):
    print("No")
