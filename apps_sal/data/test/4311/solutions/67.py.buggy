import sys
s = int(input())
f = [0 for _ in range(1000005)]
f[s] = 1
n = s
for i in range(1000005):
    if(n % 2 == 0):
        n = int(n / 2)
    else:
        n = int(3 * n + 1)
    if(f[n] == 1):
        print(i + 2)
        return
    else:
        f[n] = 1
