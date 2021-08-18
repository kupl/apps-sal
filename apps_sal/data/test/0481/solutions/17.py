__author__ = 'User'
n, x = list(map(int, input().split()))
c = 0
for i in range(max(1, x // n), n + 1):
    if x % i == 0 and x // i <= n:
        c += 1
print(c)
