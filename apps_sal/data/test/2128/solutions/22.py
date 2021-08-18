from math import gcd
M = 998244353
n = input()
p = list(map(int, input().split(' ')))
num = 0
denum = 1
for i in p:
    num = (num + denum) * 100 % M
    denum = denum * i % M
g = gcd(num, denum)
num = num // g
denum = denum // g
denum = pow(denum, M - 2, M)
print(num * denum % M)
