A, B = map(int, input().split())
if A != B:
    x = max(A, B)
    ans = 2 * x - 1
else:
    ans = 2 * A
print(ans)
