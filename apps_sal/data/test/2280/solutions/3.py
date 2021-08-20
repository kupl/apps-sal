t = int(input())
for i in range(t):
    n = int(input())
    ar = list(map(int, input().split()))
    if n <= 2:
        print(0)
        continue
    ar = sorted(ar)[::-1]
    ans = 0
    for i in range(1, n - 1):
        if ar[0] > i and ar[1] > i:
            ans = i
    print(ans)
