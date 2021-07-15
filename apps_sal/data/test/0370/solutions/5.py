import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

K = int(input())
X,Y = map(int,input().split())

if (X+Y) % 2 != 0 and K % 2 == 0:
    print(-1)
    return

def strategy(x,y,K):
    if x < 0:
        dx, dy = strategy(-x,y,K)
        return -dx, dy
    if y < 0:
        dx, dy = strategy(x,-y,K)
        return dx,-dy
    if x > y:
        dx, dy = strategy(y,x,K)
        return dy, dx
    # 0 <= x <= y としてよい
    L = x + y
    if L > 2 * K:
        dx = min(x,K)
        dy = K - dx
        return dx,dy
    # 距離2K以下。3回以内に仕留める
    if L == K:
        return x,y
    if (x+y) % 2 == 0:
        # 2回で仕留める
        # 0 <= x < y が分かっている
        t = (y - x) // 2
        dx,dy = K-t, t
        return dx,dy
    # 3回で仕留める
    # とりあえず離れないようにすればよい
    dx = min(K,x)
    dy = K - dx
    return dx,dy


x,y = 0,0
answer = []
while x != X or y != Y:
    dx,dy = strategy(X-x, Y-y, K)
    x += dx
    y += dy
    answer.append((x,y))

print(len(answer))
for x,y in answer:
    print(x,y)
