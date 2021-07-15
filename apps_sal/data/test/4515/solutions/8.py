t = int(input())
for _ in range (t):
    a, b, c, n = list(map(int, input().split()))
    d = 3 * max(a, b, c) - a - b- c
    e = n - d
    if e >= 0 and e % 3 == 0:
        print("YES")
    else:
        print("NO")
