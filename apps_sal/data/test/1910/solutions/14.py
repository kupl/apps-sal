n = int(input())
l = 2 * n - 2
t = l - n
cur1 = 4 ** t * 3
cur2 = 0
if t >= 2:
    cur2 += 4 ** (t - 1) * 9
print(cur1 * 2 + (t - 1) * cur2)
