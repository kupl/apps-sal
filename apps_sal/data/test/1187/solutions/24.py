n, m = [int(i) for i in input().split()]
data = []
chil = []
for i in range(n + 1):
    chil.append(set())
for j in range(m):
    data.append([int(i) for i in input().split()])
    chil[data[-1][0]].add(data[-1][1])

# done = set()
# fnd = set()
# cycle = False
# def dfs(a):
#     for c in chil[a]:
#         print(a,c)
#         if c in fnd:
#             nonlocal cycle
#             cycle = True
#             return
#         if c not in done:
#             fnd.add(c)
#             dfs(c)
# for i in range(1, n+1):
#     if i not in done:
#         dfs(i)
#         done |= fnd
#         fnd = set()
#         if cycle:
#             break


def cycle():
    for i in range(1, n + 1):
        stack = [i]
        fnd = [0] * (n + 1)
        while stack:
            s = stack.pop()
            for c in chil[s]:
                if c == i:
                    return True
                if not fnd[c]:
                    stack.append(c)
                    fnd[c] = 1


if not cycle():
    print(1)
    l = ['1' for i in range(m)]
    print(' '.join(l))
else:
    print(2)
    for d in data:
        print(["2", "1"][d[0] < d[1]], end=' ')
    print()
