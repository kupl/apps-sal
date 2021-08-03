N = int(input())
C = [list(map(int, input().split())) for _ in range(N - 1)]

for i in range(N - 1):
    c, s, f = C[i]
    ans = s + c
    for j in range(i + 1, N - 1):
        nc, ns, nf = C[j]
        # print('D',ans,nc,ns,nf,(ans-ns)%nf)
        ans = max(ans, ns)
        m = (ans - ns) % nf
        if m != 0:
            ans += nf - m
        # print('D',ans,nc,ns,nf,(ans-ns)%nf)
        ans += nc
    print(ans)
print(0)
