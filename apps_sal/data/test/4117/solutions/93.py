n = int(input())
n_l = list(map(int, input().split()))

ans = 0
n_l.sort()

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if n_l[i] != n_l[j] != n_l[k] and n_l[i] + n_l[j] > n_l[k]:
                ans += 1

print(ans)
