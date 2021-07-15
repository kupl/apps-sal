import math

n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
move = [a, b, c, d, e]
f = min(a, b, c, d, e)
f_index = move.index(f)+1

print(math.ceil(n/f) + (5-f_index) + f_index-1)
