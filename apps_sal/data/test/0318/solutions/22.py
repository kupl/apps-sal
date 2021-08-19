import collections
import math

#n ,m = map(int, input().split())
t = list(input())
a = int(input()) % 1440
m = (a % 60 + int(t[3]) * 10 + int(t[4])) % 60
h = (a // 60 + (a % 60 + int(t[3]) * 10 + int(t[4])) // 60 + int(t[1]) + int(t[0]) * 10) % 24
print(''.join(str(x) for x in [h // 10, h % 10, ':', m // 10, m % 10]))
