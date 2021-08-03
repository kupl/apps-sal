import sys
# from numpy import cumsum
input = sys.stdin.readline
n = int(input())
a = [int(_) for _ in input().split()]
mod = 10**9 + 7
ans = 0
s = [0]
a_ = a[::-1]
for i in range(len(a_) - 1):
    s.append(s[i] + a_[i])
s = s[::-1]
s.pop(len(s) - 1)
# print(s)
for i in range(len(a) - 1):
    ans += a[i] * s[i]
    ans = ans % mod
print(ans)
