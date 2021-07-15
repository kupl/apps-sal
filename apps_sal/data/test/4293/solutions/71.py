import itertools
P, Q, R = map(int, input().split())
lst = [P, Q, R]
c = list(itertools.combinations(lst, 2))
lst2 = []
for i in c:
    s = sum(i)
    lst2.append(s)
print(min(lst2))
