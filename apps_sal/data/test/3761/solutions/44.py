s = [len(x) for x in input().split('T')]
x, y = list(map(int, input().split()))
len_s = len(s)
sx = [s[i] for i in range(len_s) if i % 2 == 0]
sy = [s[i] for i in range(len_s) if i % 2 == 1]

x -= sx[0]
sx = sx[1:]



def is_reachable(p, s):
    origin = 8000
    if origin+p < 0:
        return False
        
    n = len(s)
    reachable = [set() for i in range(n + 1)]
    reachable[0].add(origin)

    for i in range(n):
        for j in list(reachable[i]):
            if j - s[i] >= 0:
                reachable[i + 1].add(j - s[i])
            if j + s[i] <= origin * 2:
                reachable[i+1].add(j + s[i])
    return (origin+p) in reachable[n] or (origin-p) in reachable[n]


if is_reachable(x, sx) and is_reachable(y, sy):
    print('Yes')
else:
    print('No')

