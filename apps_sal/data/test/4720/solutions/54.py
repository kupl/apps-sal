def IS(): return int(input())
def IA(): return [int(x) for x in input().split()]
def IM(N): return [IA() for _ in range(N)]


ans = 0
for l, r in IM(IS()):
    ans += r - l + 1
print(ans)
