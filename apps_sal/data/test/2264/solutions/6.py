t = int(input())
for sadf in range(t):
    n = int(input())
    max_left = 0
    min_right = 1000000000001
    for i in range(n):
        a, b = map(int, input().split())
        max_left = max(max_left, a)
        min_right = min(min_right, b)
    print(max(0, max_left - min_right))
