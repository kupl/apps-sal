from math import sqrt,floor
N,M =map(int,input().split())
ans = 1
for g in range(1,floor(sqrt(M))+1):
    if M%g == 0:
        x = M//g
        if x > floor(sqrt(M)) and g >= N:
            ans = x
            break
        if x >= N:
            ans = g
print(ans)
