N, T = map(int, input().split())
t = list(map(int, input().split()))

ans = 0
for i in range(N):
    if i == 0:
        start = t[i]
        finish = t[i] + T
        continue

    if t[i] < finish:
        finish = t[i] + T
        continue

    else:
        ans += finish - start
        start = t[i]
        finish = t[i] + T

ans += finish - start

print(ans)
