n, A, B, C, T = list(map(int, input().split()))
t = list(map(int, input().split()))
ans = A * n
if B < C:
    for time in t:
        ans += (T - time) * (C - B)
print(ans)
