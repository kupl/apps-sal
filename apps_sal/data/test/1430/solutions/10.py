(N, K) = list(map(int, input().split()))
S = input()
list10 = []
head = S[0]
cnt = 0
if S[0] == '0':
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
if S[-1] == '0':
    list10.append(0)
ans = 0
cumsum = [0]
for li in list10:
    cumsum.append(cumsum[-1] + li)
for j in range(1, len(cumsum), 2):
    h = j
    t = min(j + 2 * K, len(cumsum) - 1)
    ans = max(ans, cumsum[t] - cumsum[max(h - 1, 0)])
print(ans)
