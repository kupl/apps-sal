N=int(input())
T=list(map(int,input().split()))
V=list(map(int,input().split()))

vel_go=[0]
for ti, v_lim in zip(T,V):
    for _ in range(ti*2):
        v = min(vel_go[-1] + 0.5, v_lim)
        vel_go.append(v)

vel_back = [0]
for ti, v_lim in zip(T[::-1], V[::-1]):
    for _ in range(ti*2):
        v = min(vel_back[-1] + 0.5, v_lim)
        vel_back.append(v)
vel_back.reverse()

velocity = tuple(min(x,y) for x, y in zip(vel_go, vel_back))
ans = sum(0.25*(x+y) for x,y in zip(velocity[:-1], velocity[1:]))
print(ans)
