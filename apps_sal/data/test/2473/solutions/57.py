# coding: utf-8

# 11:50-
# 50min: give up
# 15:15-15:58 done


def main():
    N, K = list(map(int, input().split()))
    x, y = [None] * N, [None] * N
    for i in range(N):
        x[i], y[i] = list(map(int, input().split()))

    points = [[i, x[i], y[i]] for i in range(N)]
    points_ysort = sorted(points, key=lambda p: p[2], reverse=True)
    points_ysort_rev = list(reversed(points_ysort))
    points_xsort = sorted(points, key=lambda p: p[1], reverse=False)
    points_xsort_rev = list(reversed(points_xsort))

    min_area = 4 * (10**18)
    outsides_top = []

    t = 0
    while t <= N - K:
        # n_inside = N - t

        top_i, top_x, top_y = points_ysort[t]

        outsides_bottom = []
        b = 0
        while b < N:
            # n_inside -= b

            bottom_i, bottom_x, bottom_y = points_ysort_rev[b]

            if bottom_i == top_i:
                break

            # outsides_left = []
            n_outsides_left = 0
            l = 0
            while l < N:
                left_i, left_x, left_y = points_xsort[l]

                if left_x > top_x:
                    break

                if left_i in outsides_top or left_i in outsides_bottom:
                    l += 1
                    continue

                # outsides_right = []
                n_outsides_right = 0
                r = 0
                while r < N:
                    if N - t - b - n_outsides_left - n_outsides_right < K:
                        break

                    right_i, right_x, right_y = points_xsort_rev[r]

                    if right_i == left_i:
                        break

                    if right_x < top_x:
                        break

                    if right_i in outsides_top or right_i in outsides_bottom:
                        r += 1
                        continue

                    area = (top_y - bottom_y) * (right_x - left_x)
                    if area < min_area:
                        min_area = area

                    # outsides_right.append(right_i)
                    n_outsides_right += 1
                    r += 1

                # outsides_left.append(left_i)
                n_outsides_left += 1
                l += 1

            outsides_bottom.append(bottom_i)
            b += 1

        outsides_top.append(top_i)
        t += 1

    return min_area


print((main()))
