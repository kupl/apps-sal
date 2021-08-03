A, B, X = list(map(int, input().split()))


def func1(N):
    d = len(str(N))
    return A * N + B * d <= X


left = 0
right = 10**30
while left + 1 < right:
    n = (left + right) // 2
    if func1(n):
        left = n
    else:
        right = n
ans = left
print((ans if ans < 10**9 else 10**9))
