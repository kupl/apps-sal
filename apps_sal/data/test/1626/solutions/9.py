from math import ceil

n, k = list(map(int, input().split()))

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

p = 10**k

ans = 1

for i in range(n // k):
    x, y = arr1[i], arr2[i]
    a, b = y * 10**(k - 1), (y + 1) * 10**(k - 1)
    ans *= ceil(p / x) - (ceil(b / x) - ceil(a / x))
    ans %= 10**9 + 7

print(ans)
