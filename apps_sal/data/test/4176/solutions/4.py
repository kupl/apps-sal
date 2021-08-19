import math
A, B = map(int, input().split())
# A*B = l*g ,l：最小公倍数，g:最大公約数

g = math.gcd(A, B)
l = A * B // g
print(l)
