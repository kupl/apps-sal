n = int(input())
alst = list(map(int, input().split()))

ans = [0 for _ in range(n)]
pm = 1
for a in alst:
    ans[0] += a * pm
    pm *= -1
for i in range(n - 1):
    ans[i + 1] = alst[i] * 2 - ans[i]
print(*ans)
