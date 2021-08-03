from itertools import combinations_with_replacement

N, M, Q = map(int, input().split())
T = []
for q in range(Q):
    T.append(list(map(int, input().split())))

A = list(combinations_with_replacement(list(range(1, M + 1)), N))
Alist = [list(a) for a in A]

# print(Alist)

Max = 0

for a in Alist:
    cost = 0
    for t in T:
        if a[t[1] - 1] - a[t[0] - 1] == t[2]:
            cost += t[3]
    if cost > Max:
        Max = cost
print(Max)
