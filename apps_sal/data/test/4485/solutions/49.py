n, m = map(int, input().split())
arr_ = [tuple(map(int, input().split())) for _ in range(m)]

one = set([b for a, b in arr_ if a == 1])
last = set([a for a, b in arr_ if b == n])
connect = one & last
if len(connect) >= 1:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
