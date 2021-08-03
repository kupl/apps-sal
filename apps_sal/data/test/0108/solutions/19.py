s = list(input())
if len(s) < 26:
    print(-1)
    return

alpha = 'abcdefghijklmnopqrstuvwxyz'
cidx = 0

for i in range(len(s)):
    if s[i] <= alpha[cidx]:
        s[i] = alpha[cidx]
        cidx += 1
    if cidx == 26:
        print(''.join(s))
        return
else:
    print(-1)
