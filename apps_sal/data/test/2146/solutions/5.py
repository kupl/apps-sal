n = int(input())
s = [0] + list(map(int, input().split()))
ans = [0,0] + [None]*(n-1)

def bfs():
    path = [(s[1],1),(2,1)]
    while path:
        nom, pre = path.pop(0)
        if ans[nom] != None:
            continue
        ans[nom] = pre
        path.append((s[nom], pre+1))
        if nom<n:
            path.append((nom+1, pre+1))
        if nom>2:
            path.append((nom-1, pre+1))

bfs()

for j in range(1,n+1):
    print(ans[j], end=' ')

