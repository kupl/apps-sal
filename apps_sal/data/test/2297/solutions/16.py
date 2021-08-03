q = int(input())
for _ in range(q):
    l, r = list(map(int, input().split()))
    sign = -1 if l % 2 else 1
    if (r - l) % 2:
        print(-sign * (r - l + 1) // 2)
    else:
        print(sign * (l + (r - l) // 2))
