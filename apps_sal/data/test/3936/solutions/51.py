# coding: utf-8
# Your code here!
import sys
read = sys.stdin.read
readline = sys.stdin.readline

n, = map(int,readline().split())
s = input()
t = input()

MOD = 10**9+7
v = 2 # 初期状態
ans = 1
i = 0
while i < n:
    if s[i]==t[i]:
        i += 1
        if v==0:
            ans *= 2
        if v==2:
            ans *= 3
        v = 0
        ans %= MOD
    else:
        i += 2
        if v==0:
            ans *= 2
        if v==1:
            ans *= 3
        if v==2:
            ans *= 6
        v = 1
        ans %= MOD

print(ans%MOD)
