import sys
readline = sys.stdin.readline

# もっとも早い日に貪欲に働いたパターン
# もっとも遅い日に貪欲に働いたパターン
# 上記でX回目の仕事が同じ日であればその日は必ず働く必要がある

N, K, C = map(int, readline().split())
S = readline().rstrip()

fast = [0] * K
ind = 0
cnt = 0
while cnt < K:  # K回働くまで
    if S[ind] == "o":
        fast[cnt] = ind
        cnt += 1
        ind += (C + 1)
    else:
        ind += 1

late = [0] * K
ind = len(S) - 1
cnt = K - 1
while 0 <= cnt:
    if S[ind] == "o":
        late[cnt] = ind
        cnt -= 1
        ind -= (C + 1)
    else:
        ind -= 1

ans = []
for i in range(K):
    if fast[i] == late[i]:
        ans += [fast[i] + 1]

for a in ans:
    print(a)
