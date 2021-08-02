a, b, x = list(map(int, input().split()))

# 最小値
if(a % x != 0):
    min_div = a + x - (a % x)

else:
    min_div = a

# 最大値
if(b % x != 0):
    max_div = b - (b % x)

else:
    max_div = b

print((int(max((max_div - min_div + x) // x, 0))))
