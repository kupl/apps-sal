from sys import *
n = int(input())
for a in range(n // 1234567 + 1):
    for b in range((n - a * 1234567) // 123456 + 1):
        if (n - a * 1234567 - b * 123456) % 1234 == 0:
            print("YES")
            return
print("NO")
