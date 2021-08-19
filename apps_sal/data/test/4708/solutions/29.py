"""
ABC044 A 高橋君とホテルイージー
https://kenkoooo.com/atcoder/#/table/Tsukumo
"""

n = int(input())
k = int(input())
x = int(input())
y = int(input())

if n > k:
    ans = k * x + (n - k) * y
else:
    ans = n * x
print(ans)
