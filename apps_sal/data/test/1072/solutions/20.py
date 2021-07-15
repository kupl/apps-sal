read = lambda: list(map(int, input().split()))
n, m = read()
a = [input() for i in range(n)]
ans = 0
ind = [i for i in range(1, n)]
for i in range(m):
    ind2 = []
    for j in ind:
        if a[j][i] < a[j - 1][i]:
            ans += 1
            break
        elif a[j][i] == a[j - 1][i]:
            ind2.append(j)
    else:
        ind = ind2[:]
print(ans)

