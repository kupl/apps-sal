a = 1
for i in [*open(0)][1].split():
    a = [-1, (a := (a * int(i)))][-1 < a <= 1e+18]
print(a)
