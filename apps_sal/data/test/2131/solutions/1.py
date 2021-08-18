
n = int(input().strip())
degs = [0 for _ in range(n)]
for _ in range(n - 1):
    [u, v] = list(map(int, input().strip().split()))
    degs[u - 1] += 1
    degs[v - 1] += 1

ni = [None, [], [], []]
for v, d in enumerate(degs):
    dd = min(d, 3)
    ni[dd].append(v)


if len(ni[3]) > 1:
    print('No')
elif len(ni[3]) == 1:
    print('Yes')
    print(len(ni[1]))
    u = ni[3][0]
    for v in ni[1]:
        print(u + 1, v + 1)
else:
    print('Yes')
    print(1)
    print(ni[1][0] + 1, ni[1][1] + 1)
