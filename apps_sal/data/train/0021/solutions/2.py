import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    S = set(map(int, input().split()))
    ok = False
    for i in range(1, 1024):
        tmp = {i ^ val for val in S}
        if tmp == S:
            print(i)
            ok = True
            break
    if not ok:
        print(-1)
