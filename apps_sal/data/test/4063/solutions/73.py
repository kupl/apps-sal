N = int(input())
d = list(map(int, input().split()))
d = sorted(d)
if N % 2 != 0:
    print(0)
else:
    x = N // 2
    ans = d[x] - d[x - 1]
    print(ans)
