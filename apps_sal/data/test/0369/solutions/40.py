N, M = map(int, input().split())
S = input()[::-1]

if M >= N:
    print(N)
    return

p = -1
for i in reversed(range(1, M + 1)):
    if S[i] == "0":
        p = i
        break

if p == -1:
    print(-1)
    return

ps = [p]
while 1:
    tmp = -1
    for i in reversed(range(ps[-1] + 1, ps[-1] + M + 1)):
        try:
            if S[i] == "0" or i == N:
                ps.append(i)
                tmp = i
                break
        except:
            pass
    if tmp == -1:
        print(-1)
        return
    if ps[-1] == N:
        break

pp = ([ps[i + 1] - ps[i] for i in range(len(ps) - 1)])[::-1] + [ps[0]]
print(*pp)
