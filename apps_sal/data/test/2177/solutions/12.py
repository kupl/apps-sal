import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def solve():
    a,b = list(map(int, input().split()))
    B = len(str(b))-1
    if len(str(b)) != len(str(b+1)):
        B += 1
    print(a*B)

t = int(input())
for i in range(t):
    solve()

