def inpl():
    return list(map(int, input().split()))


N = int(input())
Su = inpl()
L = []
pre = 0
for s in Su:
    if s == pre:
        L[-1] += 1
    else:
        L.append(1)
        pre = s
print(2 * max([min(l, r) for (l, r) in zip(L, L[1:])]))
