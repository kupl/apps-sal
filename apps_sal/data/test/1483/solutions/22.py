n = int(input())
p = list(map(int, input().split()))

ans = list()
for i in range(n):
    co = [0 for i in range(n)]
    co[i] = 1

    k = i
    for j in range(n):
        k = p[k] - 1

        if co[k]:
            ans.append(k + 1)
            break

        co[k] += 1

print(' '.join(map(str, ans)))
