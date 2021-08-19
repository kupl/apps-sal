n = int(input())


# 長い方から買っていく
# 長さm以下は買わないとすると、条件に当てはまるのか判定する
def maruta(m):
    if n + 1 >= m * (m + 1) // 2:
        return True
    else:
        False


# 二分探索
left = 1
right = n + 1
while left + 1 < right:
    t = (left + right) // 2
    # print(left, right, t, maruta(t))
    if maruta(t):
        left = t
    else:
        right = t
    # print(left, right)
print((n + 1 - left))
