n = int(input())
d = int(input())
e = int(input())
max_d = n // d
max_e = n // e - n // e % 5
r_min = n
for i in range(0, max_e + 1, 5):
    res = n - i * e
    cur_rub = res - res // d * d
    if cur_rub < r_min:
        r_min = cur_rub
print(r_min)
