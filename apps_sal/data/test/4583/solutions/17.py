import itertools
x = input()
for v in itertools.product(['+', '-'], repeat=3):
    t = x[0] + v[0] + x[1] + v[1] + x[2] + v[2] + x[3]
    if eval(t) == 7:
        break
print(t + '=7')
