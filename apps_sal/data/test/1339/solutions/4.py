(A, B, ans) = (1000000000, 1, -1)
for i in range(1, int(input()) + 1):
    (a, b) = map(int, input().split())
    if a > A:
        if b > B:
            B = b
            ans = -1
    else:
        if b >= B:
            B = b
            ans = i
        elif a != A:
            ans = -1
        A = a
print(ans)
