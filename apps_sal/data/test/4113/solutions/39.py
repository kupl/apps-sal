import sys
n = int(input())
a = 0

for i in range((n//4)+1):
    for j in range((n//7)+1):
        a = 4*i + 7*j
        if (a == n):
            print("Yes")
            return
print("No")

