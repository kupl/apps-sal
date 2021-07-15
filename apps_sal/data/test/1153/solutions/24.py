n, m = [int(x) for x in input().split()]
ns = [int(x) for x in input().split()]
ms = [int(x) for x in input().split()]
n_summs = []
n_set = set()
m_set = set()
summa = 0
for i in range(n):
    summa += ns[i]
    n_summs.append(summa)
    n_set.add(summa)
summa = 0
m_summs = []
for j in range(m):
    summa += ms[j]
    m_summs.append(summa)
    m_set.add(summa)
print(len(n_set.intersection(m_set)))
