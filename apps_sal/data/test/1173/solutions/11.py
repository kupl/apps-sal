from collections import deque
def solve():
    n = int(input())
    a = []
    for i in range(n):
        ai = [int(j)-1 for j in input().split()]
        a.append(deque(ai))
    d = set()
    q = deque()
    for i in range(n):
        ai = a[i].popleft()
        if i < ai:
            q.append((i, ai))
        else:
            q.append((ai, i))
    ans = 0
    while q:
        ans += 1
        nxt_q = deque()
        while q:
            i, ai = q.pop()
            if (i, ai) in d:
                if a[i]:
                    ni = a[i].popleft()
                    if i < ni:
                        nxt_q.append((i, ni))
                    else:
                        nxt_q.append((ni, i))
                if a[ai]:
                    ni = a[ai].popleft()
                    if ai < ni:
                        nxt_q.append((ai, ni))
                    else:
                        nxt_q.append((ni, ai))
            else:
                d.add((i, ai))
        q = nxt_q
    if any(i for i in a):
        ans = -1
    print(ans)

solve()
