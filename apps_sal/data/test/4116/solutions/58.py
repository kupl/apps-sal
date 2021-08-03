n = int(input())
check = False
for i in range(1, 10):
    for j in range(i, 10):
        if n == i * j:
            check = True
print("Yes" if check else "No")
