n, m = map(int, input().split())
L = [i for i in range(1, m + 1)]
for j in range(n):
    l = list(map(int, input().split()))
    del l[0]
    L = set(l) & set(L)
print(len(L))
