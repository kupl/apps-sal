# author:  Taichicchi
# created: 11.10.2020 20:40:13

import sys

S = input()

K = int(input())

for i in range(K):
    if S[i] != "1":
        ans = S[i]
        break
else:
    ans = "1"

print(ans)
