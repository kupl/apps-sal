n = int(input())
p = sorted([tuple(map(int, input().split())) for _ in range(n)])
arr = list(map(int, input().split()))
w, r, pr = {}, {}, {}

for i, wi in enumerate(arr, 1):
    if wi not in w:
        w[wi] = []
    w[wi].append(i)
 
def is_nbr(nb, i):
    return 0 if pr.get(nb, 0) > i else 1

def check_nbrs(p, i):
    n1 = (p[0] - 1, p[1])
    n2 = (p[0], p[1] - 1)
    n3 = (p[0] - 1, p[1] - 1)
    return is_nbr(n1, i) and is_nbr(n2, i) and is_nbr(n3, i)

def solve():
    for i in range(len(p)):
        d = p[i][1] - p[i][0]
        if d not in w:
            return 0
        q = w[d]
        if not q:
            return 0
        ind = q.pop(0)
        r[ind] = p[i]
        pr[p[i]] = ind
        if not check_nbrs(p[i], ind):
            return 0
    return 1
 
if solve() == 0:
    print("NO")
else:
    print("YES")
    for k, v in sorted(r.items()):
        print(v[0], v[1])

