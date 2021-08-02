N, A, B = map(int, input().split())
H = [int(input()) for _ in range(N)]


def solve(k):
    cnt = 0
    for i in range(N):
        if H[i] > B * k:
            cnt += (H[i] - B * k - 1) // (A - B) + 1
    return cnt <= k


left = 0
right = 10 ** 9 + 1

while left + 1 < right:
    mid = (left + right) // 2
    if solve(mid):
        right = mid
    else:
        left = mid

print(right)
