(n, k) = map(int, input().split())
grades = list(map(int, input().split()))
ans = (2 * k - 1) * n - 2 * sum(grades)
if ans < 0:
    ans = 0
print(ans)
