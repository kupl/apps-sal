n, m = list(map(int, input().split()))
kv = [None] * 101
boo = [False] * 101
for i in range(m):
    k, j = list(map(int, input().split()))
    kv[k] = j
for j in range(1, 101):
    qw = True
    for i in range(len(kv)):
        if kv[i] is not None:
            a = (i - 1) // j + 1
            if kv[i] != a:
                qw = False
    boo[j] = qw
a = sum(boo)
first = 0
q = set()
for i in range(len(boo)):
    if boo[i]:
        q.add((n - 1) // i + 1)


if len(q) == 1:
    print(q.pop())
else:
    print(-1)
