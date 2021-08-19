N, K = list(map(int, input().split()))

num = [0] * K

for i in range(1, N + 1):
    num[i % K] += 1  # num[x] = Kで割ってx余る数が1以上N以下に何個あるか
ans = 0
for a in range(K):

    b = (K - a) % K
    c = (K - a) % K
    if (b + c) % K != 0:
        continue
    ans += num[a] * num[b] * num[c]
print(ans)
