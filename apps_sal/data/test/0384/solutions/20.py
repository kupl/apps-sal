input()

s2 = []
for el in [len(el) for el in input().strip().split('W')]:
    if el > 0: s2.append(str(el))

print(len(s2))
print(' '.join(s2))
