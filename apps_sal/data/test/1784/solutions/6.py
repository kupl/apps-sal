(n, colors) = map(int, input().split())
lens = list(map(int, input().split()))
q = [[] for i in range(n)]


def end():
    for i in range(n):
        if lens[i] != len(q[i]):
            return False
    return True


mi = min(lens)
for i in range(n):
    while len(q[i]) < min(lens[i], 1 + mi):
        q[i].append(1)
k = 1
while not end():
    k += 1
    for i in range(n):
        if len(q[i]) < lens[i]:
            q[i].append(k)
ma = max(map(max, q))
if ma <= colors:
    print('YES')
    for w in q:
        for i in w:
            print(i, end=' ')
        print()
else:
    print('NO')
