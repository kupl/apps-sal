(n, v) = (int(input()), list(sorted(map(int, input().split()))))
t = int(input())
ans = 0
for i in range(n):
    k = 0
    for j in range(i + 1, n):
        if v[j] - v[i] <= t:
            k += 1
    ans = max(ans, k + 1)
print(ans)
