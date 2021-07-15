n = int(input())
x = list(map(int, input().split()))
ans = x.copy()
b = sorted(x.copy())
k = b[0] + 1
d = {b[0]: [1, b[0]]}
for i in range(1, n):
    if b[i - 1] == b[i]:
        d[b[i]].append(k)
        k += 1
    else:
        if b[i] < k:
            d[b[i]] = [1, k]
        else:
            d[b[i]] = [1, b[i]]
            k = b[i]
        k += 1
for j in range(n):
    ans[j] = d[x[j]][d[x[j]][0]]
    d[x[j]][0] += 1
print(*ans)


