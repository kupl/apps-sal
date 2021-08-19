(n, A, B, C, T) = map(int, input().split())
t = list(map(int, input().split()))
if B >= C:
    print(A * n)
else:
    ans = A * n
    for time in t:
        ans += (C - B) * (T - time)
    print(ans)
