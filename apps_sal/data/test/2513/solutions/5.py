N = int(input())
S = input()


def f(SW, ox, prev):
    if SW == 'S':
        if ox == 'o':
            if prev == 'S': return 'S'
            else: return 'W'
        else:
            if prev == 'S': return 'W'
            else: return 'S'
    else:
        if ox == 'o':
            if prev == 'S': return 'W'
            else: return 'S'
        else:
            if prev == 'S': return 'S'
            else: return 'W'


combination = [('S', 'S'), ('S', 'W'), ('W', 'S'), ('W', 'W')]
ok = 0
for j in range(4):
    if ok == 1: break
    ans = []
    for i in range(N):
        if i == 0:
            first, last = combination[j]
            ans.append(first)
            now = first
            next_ = f(now, S[i], last)
            continue
        if i == N - 1:
            if last == next_ and first == f(next_, S[i], ans[-1]):
                ok = 1
                ans.append(next_)
                break
            else: break
        ans.append(next_)
        next_ = f(next_, S[i], ans[-2])

if ok == 1:
    print(''.join(ans))
else:
    print(-1)
