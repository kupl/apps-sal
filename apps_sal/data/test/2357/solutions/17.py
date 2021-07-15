from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())

    a = list(map(int, input().split()))
    pos = defaultdict(list)
    for i, v in enumerate(a):
        pos[v].append(i)

    ans = 10000000
    for p in pos.values():
        if len(p) <= 1:
            continue

        for i in range(len(p)-1):
            ans = min(p[i+1]-p[i]+1, ans)


    if ans==10000000:
        print(-1)
    else:
        print(ans)
