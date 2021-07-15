n = int(input())

ans = False
for i in range(1, 10):
    for j in range(1, 10):
        if i*j == n:
            ans = True

if ans == True:
    print("Yes")
elif ans == False:
    print("No")

