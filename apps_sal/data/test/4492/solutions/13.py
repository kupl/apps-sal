N, x = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for i, a in enumerate(A):
    if i == 0:
        ans += min(a, x)
        now_x = x - min(a, x)
        continue

    ans += min(a, now_x)
    now_x = x - min(a, now_x)

ans2 = 0
for i, a in enumerate(A[::-1]):
    if i == 0:
        ans2 += min(a, x)
        now_x = x - min(a, x)
        continue

    ans2 += min(a, now_x)
    now_x = x - min(a, now_x)

print(sum(A) - max(ans, ans2))
