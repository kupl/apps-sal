rr = lambda: input().strip()
rri = lambda: int(rr())
rrm = lambda: list(map(int, rr().split()))

def solve(N, S):
    ans = 0
    for i,x in enumerate(S):
        x = int(x)
        if x%2 == 0:
            ans += i + 1
    return ans


for tc in range(1):#rri()):
    N = rri()
    S = rr()
    print(solve(N, S))

