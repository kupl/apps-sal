with open(0) as f:
    N, A, B, *H = map(int, f.read().split())

diff = A - B  # 追加ダメージ
T = (max(H) + B - 1) // B  # 答えはT以下


def clearable(t):  # t回以内で敵を全滅できるか判定
    Higher = [h - B * t for h in H if h - B * t > 0]
    return True if sum([(h + diff - 1) // diff for h in Higher]) <= t else False


def binary_search(a, b, judge):  # b must be a or higher
    if a == b:
        return a, b

    c = a + (b - a) // 2
    return (a, c) if judge(c) else (c + 1, b)


a, b = 0, T
while a != b:
    a, b = binary_search(a, b, clearable)
print(a)
