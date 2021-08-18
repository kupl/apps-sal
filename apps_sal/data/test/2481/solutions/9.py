import copy
L = [[j for j in range(10)] for i in range(10)]
H, W = map(int, input().split())
costs = list()
costs2 = list()
for i in range(10):
    L1 = list(map(int, input().split()))
    costs.append(L1[1])
    costs2.append(L1[1])
    L[i] = L1
for i in range(12):
    for j in range(10):
        for k in range(10):
            costs2[j] = min(costs2[j], costs[k] + L[j][k])
    costs = copy.copy(costs2)
costs.append(0)
s = 0
for i in range(H):
    A = list(map(int, input().split()))
    s += sum([costs[i] for i in A])
print(s)
