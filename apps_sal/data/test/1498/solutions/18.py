a, b = map(int, input().split())
z = [0] * a
for _ in " " * b:
    t, k, d = map(int, input().split())
    gh = []
    for i in range(a):
        if z[i] < t:
            gh.append(i)
    if len(gh) < k:
        print(-1)
        continue
    for i in range(k):
        z[gh[i]] = t + d - 1
    print(sum(gh[:k]) + k)
