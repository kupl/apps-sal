def f(x):
    return x[1]

n = int(input())
L = []
for i in range(n):
    order = [int(s) for s in input().split()]
    L.append(order)
L = sorted(L,key=f)
last = [L[0][1]]
item = 1
while item < n:
    while item < n-1 and (L[item][1] <= last[-1] or L[item][0] <= last[-1]):
        item += 1
    if L[item][1] > last[-1] and L[item][0] > last[-1]:
        last.append(L[item][1])
    item += 1
print(len(last))
