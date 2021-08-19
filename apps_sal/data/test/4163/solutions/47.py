(N, *D) = open(0)
print('YNeos'[all((any(map(lambda c: eval(c.replace(' ', '!=')), d)) for d in zip(D, D[1:], D[2:])))::2])
