for i in [*open(0)][(a := 1)].split():
    a *= int(i)
    a = [-1, a][0 <= a <= 10 ** 18]
print(a)
