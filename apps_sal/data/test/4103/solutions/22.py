(n, b, a) = [int(x) for x in input().split()]
sun = [int(x) for x in input().split()]
a_max = a
cur_len = 0
for element in sun:
    if b == 0 and a == 0:
        break
    elif b > 0 and a < a_max and (element == 1):
        b -= 1
        a += 1
    elif a > 0:
        a -= 1
    else:
        b -= 1
    cur_len += 1
print(cur_len)
