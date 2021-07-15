O = list(input())
E = list(input())+['']
print(*[o+e for o,e in zip(O,E)], sep="")

