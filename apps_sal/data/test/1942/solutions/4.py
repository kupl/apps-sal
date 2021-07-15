def slv(n,l, r):
    l-=1
    r-=1
    c = 0
    ans = []
    for i in range(1, n):
        nl,nr = c, c + 2*(n-i)-1
        c = nr+1
        if l > nr:
            continue
        for j in range(max(l, nl), min(r, nr)+1):
            if j %2 == 0:
                ans.append(i)
            else:
                ans.append(i + (j-nl+1)//2)
    if r == n*(n-1):
        ans.append(1)
    print(' '.join([str(i) for i in ans]))


t = int(input())
for _ in range(t):
    n,l,r = list(map(int, input().split()))
    slv(n,l,r)

