IS = lambda: int(input())
IA = lambda: [int(x) for x in input().split()]
IM = lambda N: [IA() for _ in range(N)]

ans = 0
for l,r in IM(IS()):
    ans += r - l + 1
print(ans)
