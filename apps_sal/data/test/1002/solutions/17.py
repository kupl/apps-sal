n, d = list(map(int, input().split()))

L = list(map(int, input().split()))

s = sum(L)

s += 10 * (n - 1)

if(s > d):
    print(-1)
else:
    s -= 10 * (n - 1)
    print((d - s) // 5)
