N, A, B = map(int, input().split())

if A + B - 1 > N or A * B < N:
    print(-1)
    return

ans = []

x = N - A
cur = 1
while cur <= N:
    y = min(x + 1, B)
    ans += list(reversed(range(cur, cur + y)))
    cur += y
    x -= y - 1

print(*ans)
