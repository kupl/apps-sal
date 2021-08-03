def get_min(p, l, r, x):
    v = p[x - 1]
    c = 0
    for i in range(l - 1, r):
        if p[i] < v:
            c += 1
    if c == x - l:
        return True
    else:
        return False


n, m = map(int, input().split())
p = list(map(int, input().split()))
for _ in range(m):
    l, r, x = map(int, input().split())
    if x <= r and x >= l:
        if get_min(p, l, r, x):
            print('Yes')
        else:
            print('No')
    else:
        print('No')
