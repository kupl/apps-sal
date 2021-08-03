n = int(input())
a = sorted(list(map(int, input().split())))
vis = [False for i in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        if i == j:
            continue
        if a[i] < a[j] and not vis[j]:
            vis[j] = True
            break

print(sum([fact for fact in vis]))
