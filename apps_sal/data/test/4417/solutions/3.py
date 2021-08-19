for i in range(int(input())):
    (n, k) = list(map(int, input().split()))
    t = [int(i) for i in input().split()]
    r = min(t)
    s = max(t)
    if s - (s + r) // 2 > k:
        print(-1)
        continue
    print(r + k)
