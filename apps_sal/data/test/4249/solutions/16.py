(n, m) = list(map(int, input().split()))
l = list(map(int, input().split()))
l.sort(reverse=True)
ans = []


def bin(s):
    tmp = [[] for k in range(s)]
    cur = s
    tr = 0
    for i in range(n):
        if cur == s:
            cur = 0
        tmp[cur].append(l[i])
        cur += 1
    for i in range(s):
        for k in range(len(tmp[i])):
            tr += max(tmp[i][k] - k, 0)
    if tr >= m:
        return 1
    else:
        return 0


uk2 = n
uk1 = 1
while uk2 - uk1 > 1:
    if bin((uk2 + uk1) // 2):
        uk2 = (uk2 + uk1) // 2
    else:
        uk1 = (uk2 + uk1) // 2
if bin(uk1):
    print(uk1)
elif bin(uk2):
    print(uk2)
else:
    print(-1)
