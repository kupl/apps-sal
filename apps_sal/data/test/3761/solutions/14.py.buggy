import copy

s = input()
X, Y = list(map(int, input().split()))

# 少なくとも、右にx,↑にy進まなきゃいけない
# Fはくっつけられる
# s < 8000 よって N^2くらいならok
# Tが1回→左右 2回→前か後ろ 3回→左右
# この性質から、左右は左右のみで考えればいい
# x方向の数字N個をつかって、xを作成する 足し引きのみ 2^N xを加えて0にできるかどうか

s += "T"

now = 1
# 1はx方向、-1はy方向とする
start = 0
go = 0
x = []
y = []
for i in s:
    if i == "T":
        if start == 0:
            X = X - go
            go = 0
            start = 1
        else:
            if go != 0:
                if now == 1:
                    x.append(go)
                else:
                    y.append(go)
                go = 0
        now *= -1
    if i == "F":
        go += 1
x.sort()
y.sort()
x = x[::-1]
y = y[::-1]
X = abs(X)
Y = abs(Y)
x_use = sum(x) - X
y_use = sum(y) - Y
if x_use % 2 == 1 or y_use % 2 == 1 or x_use < 0 or y_use < 0:
    print("No")
    return
x_use = x_use // 2
y_use = y_use // 2


def solve(integer_list, target_sum, i=0, sum=0):
    if sum > target_sum:
        return False
    if sum == target_sum:
        return True
    if i == len(integer_list):
        return sum == target_sum
    if (solve(integer_list, target_sum, i + 1, sum)):
        return True
    if (solve(integer_list, target_sum, i + 1, sum + integer_list[i])):
        return True
    return False

# if solve(x, x_use) and solve(y, y_use):
#    print("Yes")
# else:
#    print("No")


def part_sum0(a, A):
    # 初期化
    N = len(a)
    dp = [[0 for i in range(A + 1)] for j in range(N + 1)]
    dp[0][0] = 1

    # DP
    for i in range(N):
        for j in range(A + 1):
            if a[i] <= j:  # i+1番目の数字a[i]を足せるかも
                dp[i + 1][j] = dp[i][j - a[i]] or dp[i][j]
            else:  # 入る可能性はない
                dp[i + 1][j] = dp[i][j]
    return dp[N][A]


if part_sum0(x, x_use) and part_sum0(y, y_use):
    print("Yes")
else:
    print("No")
