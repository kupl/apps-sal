from math import gcd

N = int(input())
arr = list(map(int, input().split()))

ans = arr[0]
for i in range(1, N):
    ans = gcd(ans, arr[i])
print(ans)

# gcd(0,5)=5 より ans = 0 で range(N) としてもOK
# ただgcdは最大公約数なのでgcd(0,5)=5は直感に反する
