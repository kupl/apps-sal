s = input()
T = input()

s = ''.join([x if x != '?' else '1' for x in list(s)])

start = []
for i in range(len(s) - len(T) + 1):
    tmp = 0
    for j in range(len(T)):
        if s[i + j] == T[j] or s[i + j] == '1': tmp += 1
    if tmp == len(T): start.append(i)

candidates = []
t = len(T)
ans = ''
if len(start):
    for st in start:
        tmp = s[:st] + T + s[st + t:]
        candidates.append(tmp)
    candidates.sort()
    ans = candidates[0].replace('1', 'a')
else:
    ans = 'UNRESTORABLE'

print(ans)
