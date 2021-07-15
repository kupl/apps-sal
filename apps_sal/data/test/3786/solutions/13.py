n = int(input())
p = [-1, 0] + list(map(int, input().split()))
h = [0] * (n+1)
cnt = [1] + [0] * n
for i in range(2, n+1):
    h[i] = h[p[i]] + 1
    cnt[h[i]] += 1
res = 0
for i in range(max(h)+1):
    if cnt[i] % 2 == 1:
        res += 1
print(res)

