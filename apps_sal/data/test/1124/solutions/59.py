from math import gcd

N = int(input())
arr = list(map(int, input().split()))

ans = arr[0]
for i in range(1, N):
    ans = gcd(ans, arr[i])
print(ans)
