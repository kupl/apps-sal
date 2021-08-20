t = int(input())
for _ in range(t):
    (s, i, e) = list(map(int, input().split()))
    half = (s + i + e) // 2
    maxeven = half + 1
    maxeven = max(maxeven, s)
    print(max(s + e - maxeven + 1, 0))
