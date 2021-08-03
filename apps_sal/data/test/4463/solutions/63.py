S = list(input())
T = list(input())

S.sort()
T.sort(reverse=True)

alpha = list('abcdefghijklmnopqrstuvwxyz')

check = False
cnt = 0
for s, t in zip(S, T):
    res = alpha.index(s) - alpha.index(t)
    if res < 0:
        check = True
        break
    elif res == 0:
        cnt += 1

if cnt == len(S):
    if len(S) < len(T):
        check = True

print("Yes" if check else "No")
