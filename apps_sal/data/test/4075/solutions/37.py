n, m = map(int, input().split())
line = []
for i in range(m):
    k, *s = map(int, input().split())
    line.append(list(s))
p = list(map(int, input().split()))

ans = 0
for bit in range(1 << n):
    switch = [0] * (n + 1)
    tf = 1
    for i in range(n):
        if (bit >> i) & 1:
            switch[i + 1] = 1
    for i in range(m):
        cnt = 0
        for v in line[i]:
            if switch[v]:
                cnt += 1
        if cnt % 2 != p[i]:
            tf = 0
    if tf:
        ans += 1
print(ans)
