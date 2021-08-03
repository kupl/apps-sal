import sys

N = input()

sum = 0
for i in N:
    sum += int(i)
print(("Yes" if int(N) % sum == 0 else "No"))
