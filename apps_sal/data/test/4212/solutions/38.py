(n, m, q) = map(int, input().split())
candidate = []


def gen(cur):
    if len(cur) == n:
        candidate.append(cur)
    else:
        t = cur[-1]
        for tv in range(t, m + 1):
            nex = cur[:]
            nex.append(tv)
            gen(nex)


for i in range(1, 10):
    arr = [i]
    gen(arr)
ask = []
for _ in range(q):
    ask.append(list(map(int, input().split())))
ans = 0
for cv in candidate:
    tmp = 0
    for av in ask:
        if cv[av[1] - 1] - cv[av[0] - 1] == av[2]:
            tmp += av[3]
    ans = max(ans, tmp)
print(ans)
