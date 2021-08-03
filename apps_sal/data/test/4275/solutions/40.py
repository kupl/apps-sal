a, b, *c = input()
print('YNeos'[not all(len(set(i)) == 1 for i in [c[:2], c[2:]])::2])
