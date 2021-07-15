x, y = list(map(int, input().split()))
for i in range(101):
    for j in range(101):
        if i + j == x:
            if 2*i + 4*j == y:
                print("Yes")
                return
print("No")

