def actual(O, E):
    s = ''.join([f'{o}{e}' for o, e in zip(O, E)])

    if len(O) - len(E) == 1:
        s += O[-1]

    return s

O = input()
E = input()

print(actual(O, E))
