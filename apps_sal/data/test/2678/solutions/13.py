# for _ in range(int(input())):
# dt = {} for i in x: dt[i] = dt.get(i,0)+1
#dt = {k:v for k,v in sorted(x.items(), key=lambda i: i[1])}
ipnl = lambda n: [int(input()) for _ in range(n)]
inp = lambda: int(input())
ip = lambda: [int(w) for w in input().split()]
mp = lambda: list(map(int, input().split()))

n = inp()
x = []
for i in range(n):
    x.append([int(w) for w in input().split()])
x.sort(key=lambda i: i[1])
visited = {}
ctr = 1
t = x[0]
visited[0] = 1
for i in range(1, n):
    if not visited.get(i, 0):
        visited[i] = 1
        if x[i][0] > t[1]:
            ctr += 1
            t = x[i]
print(ctr)
