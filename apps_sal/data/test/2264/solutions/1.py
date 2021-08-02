t = int(input())
for faw in range(t):
    n = int(input())
    mal = -1
    mir = 10000000000000
    for i in range(n):
        l, r = list(map(int, input().split()))
        mal = max(mal, l)
        mir = min(mir, r)
    print(max(mal - mir, 0))
