import sys
readline = sys.stdin.readline


N, K, C = map(int, readline().split())
S = readline().rstrip()

fast = [0] * K
ind = 0
cnt = 0
while cnt < K:
    if S[ind] == "o":
        fast[cnt] = ind
        cnt += 1
        ind += (C + 1)
    else:
        ind += 1

late = [0] * K
ind = len(S) - 1
cnt = 0
while cnt < K:
    if S[ind] == "o":
        late[cnt] = ind
        cnt += 1
        ind -= (C + 1)
    else:
        ind -= 1

late = late[::-1]

ans = []
for i in range(K):
    if fast[i] == late[i]:
        ans += [fast[i] + 1]

for a in ans:
    print(a)
