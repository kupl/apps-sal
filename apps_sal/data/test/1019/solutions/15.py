from math import gcd

n = int(input())
curr_opt_a = 1
for a in range(n - 1, 0, -1):
    b = n - a
    if a >= b:
        continue
    if gcd(a, b) == 1:
        curr_opt_a = max(curr_opt_a, a)
print(curr_opt_a, n - curr_opt_a)
