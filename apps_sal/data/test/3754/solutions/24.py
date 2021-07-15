import sys
input = sys.stdin.readline

ppp = 998244353
n = int(input())
d = list(map(int, input().split()))

prod = 1
sum = 0
for i in range(n):
    prod *= d[i]
    prod %= ppp
    sum += d[i]
    sum %= ppp

sum -= n
answer = prod

for i in range(n-2):
    prod *= sum - i
    prod %= ppp

print(prod)

