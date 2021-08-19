N = int(input())
dn = list(map(int, input().split()))
ans = 0
for i in range(N):
    for j in range(N):
        if i != j:
            ans += dn[i] * dn[j]
print(ans // 2)
