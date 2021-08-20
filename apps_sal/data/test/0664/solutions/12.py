n = int(input())
lst = list(map(int, input().split(' ')))
diffs = []
for t in range(len(lst) - 1):
    diffs.append(lst[t + 1] - lst[t])
diffs.append(lst[0] - lst[-1])
lista = [x for x in diffs if x < 0]
if len(lista) != 1:
    if max(diffs) == 0:
        print(0)
    else:
        print(-1)
else:
    diffs.reverse()
    index = diffs.index(lista[0])
    if index == 0:
        print(0)
    else:
        print(index)
