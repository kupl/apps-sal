import sys
input = sys.stdin.readline
(n, k) = map(int, input().split())
a = list(map(int, input().split()))
b = [0] * n
for ii in range(n):
    b[ii] = (1 + a[ii]) / 2
temp = sum(b[0:k])
ans = temp
for ii in range(n - k):
    temp += b[ii + k] - b[ii]
    if temp > ans:
        ans = temp
print(ans)
