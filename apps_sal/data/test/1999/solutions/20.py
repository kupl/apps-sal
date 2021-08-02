n = int(input())
ns = [int(x) for x in input().split()]
ind = {}
for i in range(n):
    ni = ns[i]
    while ni in ind:
        ns[ind[ni]] = None
        ind.pop(ni, None)
        ni *= 2
    ns[i] = ni
    ind[ni] = i
ans = [str(x) for x in ns if x != None]
print(len(ans))
print(' '.join(ans))
