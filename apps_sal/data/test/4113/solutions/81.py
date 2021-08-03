n = int(input())

for i in range(n + 1):
    for j in range(n + 1):
        if 4 * i + 7 * j == n:
            print("Yes")
            return
print("No")
