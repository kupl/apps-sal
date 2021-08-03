def e_golf(K, X, Y):
    # 参考: https://babcs2035.hateblo.jp/entry/2019/07/29/AtCoder_Beginner_Contest_135：E_-_Golf
    # 参考: https://atcoder.jp/contests/abc135/submissions/6607612

    # x >= y >= 0 となるようにどのような座標変換を行ったか
    is_xpos_negative = is_ypos_negative = is_swap = False
    x, y = X, Y
    if x < 0:
        x *= -1
        is_xpos_negative = True
    if y < 0:
        y *= -1
        is_ypos_negative = True
    if x < y:
        x, y = y, x
        is_swap = True

    if (x + y) % 2 == 1 and K % 2 == 0:
        return -1  # ゴールできない

    ans = []
    shot_min = max((x + y + K - 1) // K, 2)
    if (x + y) % 2 != (shot_min * K) % 2:
        shot_min += 1
    if x + y == K:
        ans.append((x, y))
    elif shot_min == 3 and x < K:
        mid = (K + x - y) // 2
        ans.extend(((x, x - K), (x + mid, y - K + mid), (x, y)))
    else:
        over = (shot_min * K - x - y) // 2
        for i in range(1, shot_min + 1):
            d = i * K
            if d <= y + over:
                ans.append((0, d))
            elif d <= y + over + x:
                ans.append((d - y - over, y + over))
            else:
                ans.append((x, y + (shot_min - i) * K))

    # 座標変換をしていた場合、元に戻す
    if is_swap:
        ans = [(second, first) for first, second in ans]
    if is_xpos_negative:
        ans = [(-first, second) for first, second in ans]
    if is_ypos_negative:
        ans = [(first, -second) for first, second in ans]
    return '\n'.join([str(len(ans))] + ['{} {}'.format(f, s) for f, s in ans])


K = int(input())
X, Y = [int(i) for i in input().split()]
print(e_golf(K, X, Y))
