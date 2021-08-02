# -*- coding: utf-8 -*-
n = int(input())
p = 10**9 + 7
k = (10**n) % p
l = (2 * 9**n) % p
m = (8**n) % p
ans = (k - l + m) % p
print(ans)
