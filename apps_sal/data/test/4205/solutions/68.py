n = int(input())
p = list(map(int, input().split()))
ans = False
for i in range(n):
    for j in range(i, n):
        (p[i], p[j]) = (p[j], p[i])
        if all((p[k] < p[k + 1] for k in range(n - 1))):
            ans = True
        (p[i], p[j]) = (p[j], p[i])
print(['NO', 'YES'][ans])
