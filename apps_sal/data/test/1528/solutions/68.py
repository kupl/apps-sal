def f(L, x):
    if L == 0:
        return 0 if x <= 0 else 1
    if x <= total[L - 1] + 1:
        return f(L - 1, x - 1)
    else:
        return patties[L - 1] + 1 + f(L - 1, x - total[L - 1] - 2)


N, X = list(map(int, input().split()))
total = [1]
patties = [1]
for i in range(50):
    total.append(total[-1] * 2 + 3)
    patties.append(patties[-1] * 2 + 1)
print((f(N, X)))

