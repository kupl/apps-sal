n,m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
cd = [list(map(int, input().split())) for _ in range(m)]

for a,b in ab:
    ans = []
    for c,d in cd:
        ans.append(abs(a-c)+abs(b-d))
    print(ans.index(min(ans))+1)
