import math
n = int(input())
a = list(map(int, input().split()))
a.sort()
hsh = [1] + [0] * (max(a) + 1)
for i in a:
    if hsh[i - 1] == 0:
        hsh[i - 1] = 1
    elif hsh[i] == 0:
        hsh[i] = 1
    elif hsh[i + 1] == 0:
        hsh[i + 1] = 1
print(hsh.count(1) - 1)
