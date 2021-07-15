result = False
n = int(input())
for i in range(1, 10):
    for j in range(1, 10):
        if i * j == n:
            result = True
            break

if result:
    print("Yes")
else:
    print("No")

