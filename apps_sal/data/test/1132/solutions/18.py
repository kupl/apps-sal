(n, m) = list(map(int, input().split()))
vs = [0 for i in range(n)]
for i in range(m):
    (x, y) = list(map(int, input().split()))
    vs[x - 1] = vs[x - 1] + 1
    vs[y - 1] = vs[y - 1] + 1
if max(vs) == m and n == m + 1:
    print('star topology')
else:
    ones = sum([1 if x == 1 else 0 for x in vs])
    if n == m + 1 and ones == 2:
        print('bus topology')
    else:
        doubles = sum([1 if x == 2 else 0 for x in vs])
        if n == m and doubles == n:
            print('ring topology')
        else:
            print('unknown topology')
