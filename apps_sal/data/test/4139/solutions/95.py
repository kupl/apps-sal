import itertools

n = int(input())

products = []
for i in range(3, len(str(n)) + 1):
    tmp = list(itertools.product(['3', '5', '7'], repeat = i))
    tmp2 = list(map(''.join, tmp))
    tmp3 = list(map(int, tmp2))
    tmp4 = [j for j in tmp3 if j <= n]
    products = products + tmp4

out = 0
for p in products:
    str_p = str(p)
    if ('3' in str_p) and ('5' in str_p) and ('7' in str_p):
        out += 1
print(out)
