n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

need = sorted(a, reverse=True)

ind = list()
for el in need[:k]:
    ind.append(a.index(el))
    a[a.index(el)] = 0

ind.sort()

print(sum(need[:k]))

ind[-1] = n - 1
ind.insert(0, -1)
ans = [el - ind[i] for i, el in enumerate(ind[1:])]

print(' '.join(map(str, ans)))

