(A, B, ans) = (1000000000, 1, -1)
for i in range(1, int(input()) + 1):
    (a, b) = map(int, input().split())
    if a > A:
        if b > B:
            (B, ans) = (b, -1)
    elif b >= B:
        (A, B, ans) = (a, b, i)
    elif a != A:
        (A, ans) = (a, -1)
print(ans)
