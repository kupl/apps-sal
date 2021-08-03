from collections import deque

N = int(input())
S = list(map(int, input().split()))
S.sort()

used = [S.pop()]
for _ in range(N):

    l, r = 0, len(used)
    reuse = deque()
    for i in range(len(S)):
        v = S.pop()
        if v < used[l]:
            used.append(v)
            l += 1
        else:
            reuse.appendleft(v)
        if l == r:
            break
    else:
        print('No')
        break
    S.extend(reuse)
    used.sort(reverse=True)
else:
    print('Yes')
