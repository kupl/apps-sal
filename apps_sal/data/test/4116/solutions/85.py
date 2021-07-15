n = int(input())
a = 0

for i in range(10):
    for j in range(10):
        a = i*j
        if (a == n):
            print("Yes")
            return
print("No")

