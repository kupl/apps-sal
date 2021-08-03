X = int(input())
exps = []
for b in range(1, 34):
    for p in range(2, 11):
        x = b**p
        if x < 1001:
            exps.append(x)
exps = list(set(exps))
exps.sort()
for a in exps[::-1]:
    if X >= a:
        print(a)
        break
