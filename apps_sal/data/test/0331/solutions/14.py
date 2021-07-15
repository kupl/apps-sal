#!/bin/python3

import sys
n, m , k = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = n ;
for i in range(n):
    if a[i] != 0 and a[i] <= k and ans > abs(m - i - 1):
        ans = abs(m - i - 1)
print(ans*10)

