N = int(input())
W = list(input() for i in range(N))

W_len = len(W)

import sys
for i in range(0,W_len):
    n = i + 1
    while n <= W_len - 1:
        if W[i] == W[n]:
            print("No")
            return
        else:
            n += 1

x = 0
while x <= W_len - 2:
    if not W[x][-1] == W[x + 1][0]:
        print("No")
        return
    else:
        x += 1
print("Yes")



