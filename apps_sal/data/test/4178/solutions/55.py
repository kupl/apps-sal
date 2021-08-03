import sys

N = int(input())
H = [int(n) for n in input().split()][::-1]


for i in range(N - 1):
    if H[i + 1] - H[i] > 1:
        print('No')
        return
        break
    elif H[i + 1] - H[i] == 1:
        H[i + 1] -= 1
    else:
        continue

print('Yes')
