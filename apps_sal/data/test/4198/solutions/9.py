A, B, X = map(int, input().split())


def price(N):
    return A * N + B * len(str(N))


left = 0
right = 10**9 + 1
while right - left > 1:
    mid = (left + right) // 2
    if price(mid) <= X:
        left = mid
    else:
        right = mid

print(left)
