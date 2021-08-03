import sys
3
def input(): return sys.stdin.readline().strip()


x, y = [int(x) for x in input().split()]
ans = 0
while x <= y:
    ans += 1
    x *= 2
print(ans)
