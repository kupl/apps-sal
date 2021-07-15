read = lambda: list(map(int, input().split()))
n = int(input())
p = [list() for i in range(367)]
for i in range(n):
    s, a, b = input().split()
    a, b = list(map(int, (a, b)))
    p[a].append((1, s))
    p[b].append((-1, s))
cntm = cntf = cur = ans = 0
for i in range(1, 367):
    for t, s in p[i]:
        if t == 1:
            if s == 'M': cntm += 1
            else: cntf += 1
    cur = min(cntf, cntm)
    #print(i, cur, cntf, cntm)
    ans = max(ans, cur)
    for t, s in p[i]:
        if t == -1:
            if s == 'M': cntm -= 1
            else: cntf -= 1
print(ans * 2)


