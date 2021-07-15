from sys import stdin
n=int(stdin.readline().strip())
if n==3:
    print("1 2 3")
    return
adj=[(0,0)]

for i in range(n):
    a,b=list(map(int,stdin.readline().strip().split()))
    adj.append((a,b))
s=[]
x=1

while len(s)<n:
    if adj[x][0] in adj[adj[x][1]]:
        s.append(adj[x][1])
        s.append(adj[x][0])
        x=adj[x][0]
    if adj[x][1] in adj[adj[x][0]]:
        s.append(adj[x][0])
        s.append(adj[x][1])
        x=adj[x][1]
print(*s[0:n])

