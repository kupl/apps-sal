import sys

def unhoppable(p, n):
    for d in range(2, n+1):
        if p % d == 0:
            return False
        if d*d > p:
            break
    return True

p, y = list(map(int, input().split()))
for b in range(y, p, -1):
    if unhoppable(b, p):
        print(b)
        return
print(-1)

