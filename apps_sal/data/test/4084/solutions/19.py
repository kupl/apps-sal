(N, A, B) = map(int, input().split())
ans = N // (A + B) * A
left = N % (A + B)
if left <= A:
    print(ans + left)
else:
    print(ans + A)
