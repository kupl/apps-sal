from collections import deque
N = int(input())
S = input()
T = [deque([0, 0]),
     deque([0, 1]),
     deque([1, 0]),
     deque([1, 1])]
for s in S:
    for t in T:
        l = len(t)
        if (s == 'o') ^ t[l - 1]:
            t.append(t[l - 2])
        else:
            t.append(t[l - 2] ^ 1)

ans = '-1'
def wrap(x): return '{' + str(x) + '}'


for t in T:
    if t[0] == t[N] and t[1] == t[N + 1]:
        t.pop()
        t.popleft()
        ans = ''.join(wrap(i) for i in t).format('S', 'W')
        break
print(ans)
