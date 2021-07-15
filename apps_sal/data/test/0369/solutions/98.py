N, M = map(int, input().split())
S = input()
ans = []
tmp = S[::-1]
index = 0
acnt = M
while True:
    if acnt == 0:
        print(-1)
        return
    if index + acnt <= N and tmp[index + acnt] == '0':
        ans.append(acnt)
        index += acnt
        acnt = M
    else:
        acnt -= 1
    if index == N:
        break
print(*reversed(ans))
