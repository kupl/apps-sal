n, m, k = list(map(int, input().split()))
l = list(map(int, input().split()))
for i in range(n):
    l[i] = [l[i], i]
l.sort()

uk1 = 1
uk2 = n

def pos(n):
    cnt = [-10000000001] * len(l)
    nonlocal k
    for i in range(len(l)):
        if l[i][0] - cnt[i % n] <= k:
            return False
        else:
            cnt[i % n] = l[i][0]

    return True
while uk2 - uk1 > 1:
    if pos((uk2 + uk1) // 2):
        uk2 = (uk1 + uk2) // 2
    else:
        uk1 = (uk1 + uk2) // 2

ans = [0] * n
if not pos(uk1):
    for i in range(n):
        ans[l[i][1]] = i % uk2 + 1
    print(uk2)
    for i in range(n):
        print(ans[i], end =' ')
else:
    for i in range(n):
        ans[l[i][1]] = i % uk1 + 1
    print(uk1)
    for i in range(n):
        print(ans[i], end =' ')
