n = int(input())
a = [[q * (n - q1) * (q1 + 1), q1] for q1, q in enumerate(list(map(int, input().split())))]
s = sorted(list(map(int, input().split())), reverse=True)
d = sorted(a)
ans = [0] * len(s)
for q in range(n):
    ans[d[q][1]] = s[q]
print(sum(a[q][0] * ans[q] for q in range(n)) % 998244353)
