import sys

n = int(input())

for a in range(1, 10):
    for b in range(1, 10):
        if a * b == n:
            print("Yes")
            return
print("No")
