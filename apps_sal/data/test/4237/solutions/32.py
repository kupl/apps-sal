import math
A, B, C, D = map(int, input().split())

# for文は間に合わないので、包除原理を使え！

# CでもDでも割り切れない =
# 全体(a) - Cで割り切れる(b) + Dで割り切れる(c)
# + CでもDでも割り切れる(d)

# Cで割り切れる個数 =
# B以下の数でCで割り切れる個数 - (A−1)以下の数でCで割り切れる個数

lcm = C * D // math.gcd(C, D)
a = B - A + 1
b = B // C - (A - 1) // C
c = B // D - (A - 1) // D
d = B // lcm - (A - 1) // lcm

print(a - b - c + d)
