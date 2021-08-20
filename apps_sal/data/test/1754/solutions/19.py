(n, m, k) = list(map(int, input().split()))
p = list(map(int, input().split()))
s = list(map(int, input().split()))
c = list(map(int, input().split()))
sc = [-1 for i in range(m)]
for i in range(n):
    if sc[s[i] - 1] == -1 or p[sc[s[i] - 1]] <= p[i]:
        sc[s[i] - 1] = i
ans = 0
for i in range(k):
    ans += 0 if c[i] - 1 in sc else 1
print(ans)
