import itertools

n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

# generate permunations from Node 2 to Node n
p = itertools.permutations(range(2, n + 1), n - 1)

cnt = 0
for v in p:
    if [1, v[0]] not in ab and [v[0], 1] not in ab:
        continue
    else:
        if all([n0, n1] in ab or [n1, n0] in ab for n0, n1 in zip(v, v[1:])):
            cnt += 1
print(cnt)
