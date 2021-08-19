q = int(input())
for case in range(q):
    (a, b, c) = list(map(int, input().split()))
    sm = abs(c - a) + abs(b - a) + abs(b - c)
    ans = max(0, sm - 4)
    print(ans)
