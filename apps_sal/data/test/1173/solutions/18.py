from collections import deque
n = int(input())
def x(i): return int(i) - 1


a = [deque(list(map(x, input().split())) + [-1]) for _ in range(n)]
tcnt, ans = n * (n - 1), 0
chk = set(range(n))
while tcnt > 0:
    chk_next = set()
    for i in chk:
        if a[a[i][0]][0] == i:
            chk_next.add(i)
    if len(chk_next) == 0:
        ans = -1
        break
    tcnt -= len(chk_next)
    chk = set()
    for i in chk_next:
        a[i].popleft()
        chk.add(i)
        if a[i][0] != -1:
            chk.add(a[i][0])
    ans += 1

print(ans)
