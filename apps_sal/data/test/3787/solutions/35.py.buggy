# coding: utf-8
# Your code here!
import sys
readline = sys.stdin.readline
read = sys.stdin.read

n, a, b = list(map(int, input().split()))

if n < a + b - 1 or n > a * b:
    print((-1))
    return

ans = list(range(n, 0, -1))
if a == 1:
    print((*ans))
    return
k = (a * b - n) // (a - 1)
v = n - k - a * (b - k - 1)

# print(a,b,n,k,v)
i = -1
for i in range(b - k - 1):
    ans[i * a:(i + 1) * a] = ans[i * a:(i + 1) * a][::-1]
i += 1
ans[i * a:i * a + v] = ans[i * a:i * a + v][::-1]

print((*ans))
