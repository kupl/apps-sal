import math

n, k = map(int, input().split())
log2 = math.log10( 2)
ans = 0
for i in range(1,n+1):
    temp = i
    num = 1/n
    while temp < k:
        num /= 2
        temp *= 2
    ans += num

print(ans)
