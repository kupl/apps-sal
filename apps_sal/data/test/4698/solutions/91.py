n = int(input())
t = list(map(int,input().split()))
m = int(input())
px = [list(map(int,input().split())) for _ in range(m)]
for i in px:
    print((sum(t) - t[i[0]-1] + i[1]))

