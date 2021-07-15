from sys import *
n = int(stdin.readline())
ans = 0
for i in range(2,n+1):
    for j in range(i*2,n+1,i):
        ans += 4 * (j // i)
print(ans)

