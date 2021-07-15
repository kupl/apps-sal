S = input()
T = input()

for i, j in zip(S, T[:-1]):
    if i != j:
        print('No')
        break
else:
    print('Yes')
