import sys
n = int(input())
for i in range(int(n / 4) + 1):
    for j in range(int(n / 7) + 1):
        if 4 * i + 7 * j == n:
            print('Yes')
            return
print('No')
