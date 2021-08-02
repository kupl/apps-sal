n = int(input())
l = list(map(int, input().split()))
d = {}
for i in l:
    if i not in d:
        d[i] = 0
    d[i] += 1
ans = 0
for i in range(len(l)):
    for j in range(len(l)):
        if i == j:
            continue
        n1, n2 = l[i], l[j]
        if n1 == 0 and n2 == 0:
            continue
        curr = 2
        d2 = {n1: 1, n2: 1}
        while True:
            n1, n2 = n2, n1 + n2
            ans = max(ans, curr)
            if n2 in d and (d2[n2] if n2 in d2 else 0) < d[n2]:
                if n2 not in d2:
                    d2[n2] = 0
                d2[n2] += 1
                curr += 1
            else:
                break
print(max(ans, (d[0] if 0 in d else -1)))
