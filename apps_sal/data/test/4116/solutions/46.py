import sys
n = int(input())
for i in range(1, 10):
    for j in range(1, 10):
        if i * j == n:
            print("Yes")
            return
print("No")
