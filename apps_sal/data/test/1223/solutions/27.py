N = int(input())
*P, = map(int, input().split())

LL = [0] + [i for i in range(N+1)]
RR = [i+1 for i in range(N+1)] + [N+1]

E = [(v, i+1) for i, v in enumerate(P)]
E.sort()

ans = 0
for v, i in E:
    l0 = LL[i]; l1 = LL[l0]

    r0 = RR[i]; r1 = RR[r0]

    LL[RR[i]], RR[LL[i]] = LL[i], RR[i]

    ans += ((r1 - r0) * (i - l0) + (r0 - i) * (l0 - l1)) * v
print(ans)
