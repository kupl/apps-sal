from collections import Counter
n = int(input())
c = list(input())
num = Counter(c)
r = num['R']
ans = ['R'] * r + ['W'] * (n - r)
cnt = 0
for i in range(n):
    if c[i] != ans[i]:
        cnt += 1
print(cnt // 2)
