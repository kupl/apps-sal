N, K, C = map(int, input().split())
S = input()
dp0 = [0] * K
dp1 = [0] * K
step = C
cnt = 0
for i in range(N):
    if step >= C and S[i] == 'o':
        dp0[cnt] = i
        cnt += 1
        if cnt == K:
            break
        step = 0
    else:
        step += 1
step = C
cnt = K - 1
for i in range(N - 1, -1, -1):
    if step >= C and S[i] == 'o':
        dp1[cnt] = i
        cnt -= 1
        if cnt == -1:
            break
        step = 0
    else:
        step += 1
ans = 0
for i, (a, b) in enumerate(zip(dp0, dp1)):
    if a == b:
        print(a + 1)
