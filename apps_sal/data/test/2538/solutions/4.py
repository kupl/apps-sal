T = int(input())
for t in range(T):
    s, i, e = list(map(int, input().split()))
    min_s = max((s + i + e) // 2 + 1, s)
    max_s = s + e
    c = max(0, max_s - min_s + 1)
    print(c)
