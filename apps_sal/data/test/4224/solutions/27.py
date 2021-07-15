import math

N = int(input())
a = list(map(int,input().split()))
ans = 0

for i in a:
    while True:
        if i %2==0:
            i = i/2
            ans += 1
        else:
            break

print(ans)

