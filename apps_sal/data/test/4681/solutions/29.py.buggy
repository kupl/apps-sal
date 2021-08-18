import sys
N = int(input())
if(N == 1):
    print(1)
    return
ans = 0
L0 = 2
L1 = 1
for i in range(N - 1):
    ans = L0 + L1
    L0 = L1
    L1 = ans
print(ans)
