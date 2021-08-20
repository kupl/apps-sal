def getdiff(a, b):
    return sum([a[i] != b[i] for i in range(n)])


(n, m, k) = list(map(int, input().split()))
armies = [0 for i in range(m)]
for i in range(m):
    armies[i] = bin(int(input()))[2:].rjust(n, '0')
ans = 0
M = bin(int(input()))[2:].rjust(n, '0')
for i in range(m):
    if getdiff(M, armies[i]) <= k:
        ans += 1
print(ans)
