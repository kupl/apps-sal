from fractions import gcd

def lcm(a, b):
    return (a * b) // gcd(a, b)

n = int(input())
go = list(map(int, input().split()))
for i in range(n):
    go[i] -= 1
vis = [False for i in range(n)]
ans = 1
for i in range(n):
    vis = [False for j in range(n)]
    x = go[i]
    while True:
        if vis[x] == True:
            break
        vis[x] = True
        x = go[x]
    if vis[i] == False:
        print("-1")
        return
vis = [False for i in range(n)]
for i in range(n):
    if vis[i] == True:
        continue
    x = i
    cycle = 0
    while True:
        if vis[x] == True:
            break
        cycle += 1
        vis[x] = True
        x = go[x]
    if cycle % 2 == 1:
        ans = lcm(ans, cycle)
    else:
        ans = lcm(ans, cycle // 2)
print(ans)

