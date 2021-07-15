S = input()
T = ['dream', 'dreamer', 'erase', 'eraser']

rS = str(S[:: -1])
rT = [str(t[:: -1]) for t in T]

now = 0
while now < len(S):
    for t in rT:
        if t == rS[now: now + len(t)]:
            now += len(t)
            break
    else:
        print('NO')
        return

print('YES')

