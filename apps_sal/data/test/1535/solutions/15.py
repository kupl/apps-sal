(n, x, y) = list(map(int, input().split()))
's_x=[]\ns_y=[]'
shots = set()
for _ in range(n):
    's_x[i],s_y[i] = map(int,input().split())\n    s_x[i] -= x\n    s_y[i] -= y'
    (a, b) = list(map(int, input().split()))
    a -= x
    b -= y
    shots.add('INF' if a == 0 else b / a)
print(len(shots))
