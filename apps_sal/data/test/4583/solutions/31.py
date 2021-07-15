from itertools import product


A, B, C, D = list(input())
for x, y, z in product(["+", "-"], repeat=3):
    eqn = A + x + B + y + C + z + D
    if eval(eqn) == 7:
        print(f"{eqn}=7")
        break
