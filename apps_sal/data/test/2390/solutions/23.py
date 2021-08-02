import sys

N, C = map(int, sys.stdin.readline().split())

sushi_set = []
for i in range(N):
    x, v = map(int, sys.stdin.readline().split())
    sushi_set.append((x, v))
sushi_set.sort()

ans = -1

# 方向転換は一回まででと考えて良いのではないか？
# right
right = [0 for _ in range(N)]
max_n = -float("inf")
energy = 0
right_back = [0 for _ in range(N)]
for i, (x, v) in enumerate(sushi_set):
    energy += v
    if energy - x > max_n:
        max_n = energy - x
    right[i] = max_n
    right_back[i] = energy - 2 * x

# left
left = [0 for _ in range(N)]
max_n = -float("inf")
energy = 0
left_back = [0 for _ in range(N)]
for i, (x, v) in enumerate(sushi_set[::-1]):
    energy += v
    if energy - (C - x) > max_n:
        max_n = energy - (C - x)
    left[i] = max_n
    left_back[i] = energy - 2 * (C - x)

# print("right", right)
# print("right_back", right_back)
# print("left", left)
# print("left_back", left_back)

ans = max(max(right), max(left))
# print(ans)
# right -> left
for i in range(N - 1):
    ans = max(ans, right_back[i] + left[N - 2 - i])
# left -> right
for i in range(N - 1):
    ans = max(ans, left_back[i] + right[N - 2 - i])

print(max(ans, 0))
