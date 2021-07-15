N = int(input())
P = [(0,0,0)] + [tuple(int(x) for x in input().split()) for _ in range(N)]

def travelable(p,q):
    time = q[0] - p[0]
    dist = abs(q[1]-p[1]) + abs(q[2]-p[2])
    if dist <= time and time%2 == dist%2:
        return True
    else:
        return False
        
print('Yes' if all(travelable(p,q) for p,q in zip(P[:N],P[1:])) else 'No')
