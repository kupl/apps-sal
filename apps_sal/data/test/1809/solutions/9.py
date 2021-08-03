a, b = list(map(int, input().split(' ')))
c = list(map(int, input().split(' ')))
d = list(map(int, input().split(' ')))
e = []
dictx = {}
for i in range(1, a + 1):
    dictx[i] = c[i - 1]
for i in d:
    if i not in e:
        e.append(i)

tot = 0
for i in d:
    indx = e.index(i)
    tot += sum([dictx[i] for i in e[:indx]])
    e = [e[indx]] + e[:indx] + e[indx + 1:]
print(tot)
