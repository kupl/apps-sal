n, k = map(int, input().split())
i = 1
n -= k
while n > 0 and not(bin(n).count('1') <= i <= n):
    n -= k
    i += 1
if n > 0:
    print(i)
else:
    print(-1)
