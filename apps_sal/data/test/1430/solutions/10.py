N, K = list(map(int, input().split()))
S = input()

# 1の個数, 0の個数, 1の個数, ..., 1の個数
list10 = []
head = S[0]
cnt = 0

# 左端の1の数
if S[0] == "0":
    list10.append(0)

for i in range(N):
    if S[i] == head:
        cnt += 1
    else:
        list10.append(cnt)
        cnt = 1
        head = S[i]

    if i == N - 1:
        list10.append(cnt)

# 右端の1の数
if S[-1] == "0":
    list10.append(0)

# print(list10)

ans = 0

cumsum = [0]
for li in list10:
    cumsum.append(cumsum[-1] + li)
# print(cumsum)

for j in range(1, len(cumsum), 2):
    h = j
    t = min(j + 2 * K, len(cumsum) - 1)
    ans = max(ans, cumsum[t] - cumsum[max(h - 1, 0)])
print(ans)

