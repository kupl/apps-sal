(W, a, b) = list(map(int, input().split()))
if abs(a - b) <= W:
    print(0)
else:
    print(abs(a - b) - W)
