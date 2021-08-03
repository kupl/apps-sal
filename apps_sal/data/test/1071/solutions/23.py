from math import ceil
a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())
n = int(input())
print('YES') if ceil((a1 + a2 + a3) / 5) + ceil((b1 + b2 + b3) / 10) <= n else print('NO')
