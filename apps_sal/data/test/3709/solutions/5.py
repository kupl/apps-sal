n, k = list(map(int, input().split()))
sp = [0] * (2**k)
for i in range(n):
    ci = list(map(int, input().split()))
    c = 0
    for j in range(k - 1, -1, -1):
        c += (1 - ci[j]) * (2**j)
    sp[c] += 1
ed = [False] * k
for i in range(2**k - 1, -1, -1):
    ci = []
    t = i
    for j in range(k - 1, -1, -1):
        ci.append(t // (2**j))
        t %= 2**j
    if sp[i] > 0:
        for j in range(k):
            if ci[j] == 1:
                ed[j] = True
        break
p = i - 1
for i in range(p, -1, -1):
    ci = []
    t = i
    for j in range(k - 1, -1, -1):
        ci.append(t // (2**j))
        t %= 2**j
    if sp[i] > 0:
        for j in range(k):
            if not(ci[j] == 1 or ed[j]):
                break
        else:
            print('YES')
            return
if sp[2**k - 1] > 0:
    print('YES')
else:
    print('NO')
