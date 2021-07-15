arri = lambda: [int(s) for s in input().split()]

n, m = arri()
p = arri()
ans = []
for i in range(m):
    l, r, x = arri()
    no = l - 1
    cur = p[x-1]
    for i in range(l - 1, r):
        if p[i] < cur:
            no -=- 1
    ans.append('Yes' if no == x- 1 else 'No')
print('\n'.join(ans))
