N, M = map(int, input().split())
S = input()
S = S[::-1]
now = 0
ok = 1
history = []
while True:
    for i in range(min(M, N - now), 0, -1):
        if S[now + i] == '0':
            now += i
            history.append(str(i))
            break
        if i == 1:
            print(-1)
            ok = 0
            break
    if ok == 0: break
    if now == N: break

if ok == 1: print(' '.join(history[::-1]))
