n,m = map(int,input().split())
path = [[[],[],[]] for i in range(n)]

gone = [[0]*3 for i in range(n)]
for i in range(m):
    u,v = map(int,input().split())
    path[u-1][0].append([v-1,1])
    path[u-1][1].append([v-1,2])
    path[u-1][2].append([v-1,0])

s,t = map(int,input().split())

now = [[s-1,0]]
gone[s-1][0] = 1
for ans in range(1,1000000):
    next = []
    for point,key in now:
        for go,gokey in path[point][key]:
            if go == t-1 and gokey == 0:
                print(ans//3)
                return
            if gone[go][gokey] == 0:
                gone[go][gokey] = 1
                next.append([go,gokey])
    now = next
  #     print(now)
print(-1)
