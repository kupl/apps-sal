from fractions import gcd
n = int(input())
arr = list(map(int, input().split()))
ans = arr[0]
for i in range(1, len(arr)):
    ans = gcd(ans, arr[i])
print(ans * len(arr))
