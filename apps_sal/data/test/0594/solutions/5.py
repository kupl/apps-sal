n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(244):
    c1 = 0
    c2 = 0
    c3 = 0
    for aa in a:
        if aa <= i:
            c1 += 1
        if 2 * aa <= i:
            c2 = 1
    for bb in b:
        if bb > i:
            c3 += 1
    if(c1 == n and c2 > 0 and c3 == m):
        print(i)
        break
else:
    print(-1)
