N, K = list(map(int, input().split()))
p = list(map(int, input().split()))
s = 0
hoge = 0
ans = 0
for i in range(K):
    s += p[i]
    temp = s
for j in range(N - K):
    s = s - p[j] + p[j + K]
    if temp < s:
        temp = s
        hoge = j + 1

for k in range(K):
    ans += (1 + p[hoge + k]) / 2

print(ans)
