K = int(input())
X, Y = map(int, input().split())

sgn_X, sgn_Y = 1, 1
if X < 0:
    X = -X
    sgn_X = -1
if Y < 0:
    Y = -Y
    sgn_Y = -1

if K % 2 == 0 and (X + Y) % 2 == 1:
    print(-1)
else:
    xx, yy = 0, 0
    vec_list = []
    while((X - xx) + (Y - yy) > 2 * K):
        if X - xx > K:
            xx += K
            vec_list.append((K, 0))
        elif Y - yy > K:
            yy += K
            vec_list.append((0, K))
    diff_x = X - xx
    diff_y = Y - yy

    if diff_x + diff_y == K:
        vec_list.append((diff_x, diff_y))
    else:
        if (diff_x + diff_y) % 2 == 1:
            if diff_x <= K:
                xx += diff_x
                if K - diff_x < diff_y:
                    yy += K - diff_x
                    vec_list.append((diff_x, K - diff_x))
                else:
                    yy -= K - diff_x
                    vec_list.append((diff_x, -K + diff_x))
            elif diff_y <= K:
                yy += diff_y
                if K - diff_y < diff_x:
                    xx += K - diff_y
                    vec_list.append((K - diff_y, diff_y))
                else:
                    xx -= K - diff_y
                    vec_list.append((-K + diff_y, diff_y))
            diff_x = X - xx
            diff_y = Y - yy

        buf = 2 * K - (diff_x + diff_y)
        if diff_x + buf // 2 <= K:
            vec_list.append((diff_x + buf // 2, K - (diff_x + buf // 2)))
            vec_list.append((-buf // 2, K - buf // 2))
        elif diff_y + buf // 2 <= K:
            vec_list.append((K - (diff_y + buf // 2), diff_y + buf // 2))
            vec_list.append((K - buf // 2, -buf // 2))
        else:
            raise("Error")

    print(len(vec_list))
    pos_x, pos_y = 0, 0
    for x, y in vec_list:
        pos_x += sgn_X * x
        pos_y += sgn_Y * y
        print(pos_x, pos_y)
