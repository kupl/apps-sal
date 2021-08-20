(n, m) = map(int, input().split())
friend = [[] for i in range(n)]
for i in range(m):
    (u, v) = map(int, input().split())
    friend[u - 1].append(v - 1)
    friend[v - 1].append(u - 1)
step = [len(friend[i]) for i in range(n)]
s = set()
ans = 0
ass = s.add
for i in range(n):
    if i in s:
        continue
    Q = i
    k = 1
    ass(Q)
    while True:
        if step[Q] != 2:
            ass(Q)
            break
        elif friend[Q][0] not in s:
            Q = friend[Q][0]
            ass(Q)
            k += 1
        elif friend[Q][1] not in s:
            Q = friend[Q][1]
            ass(Q)
            k += 1
        elif friend[Q][0] == i or friend[Q][1] == i:
            if k > 2:
                ans += 1
            break
        else:
            ass(Q)
            break
print(ans)
