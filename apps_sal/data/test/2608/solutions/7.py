def num_sq(x, y, x2, y2):
    # b, w
    a = (abs(x2 - x) + 1)
    b = (abs(y2 - y) + 1)
    if a % 2 == 0 or b % 2 == 0:
        return (a * b // 2, a * b // 2)
    if (x + y) % 2 == 0:
        num_b = a * b // 2
        return (num_b, a * b - num_b)
    num_w = a * b // 2
    return (a * b - num_w, num_w)


def pt_in(p1, r1, r2):
    return r1[0] <= p1[0] <= r2[0] and r1[1] <= p1[1] <= r2[1]


def intc(p1, p2, p3, p4):
    x1 = max(p1[0], p3[0])
    x2 = min(p2[0], p4[0])
    y1 = max(p1[1], p3[1])
    y2 = min(p2[1], p4[1])
    if x1 <= x2 and y1 <= y2:
        return ((x1, y1), (x2, y2))
    return None


num_ = int(input())
for _ in range(num_):
    n, m = list(map(int, input().split()))
    x1, y1, x2, y2 = list(map(int, input().split()))
    x3, y3, x4, y4 = list(map(int, input().split()))
    p1 = (x1, y1)
    p2 = (x2, y2)
    p3 = (x3, y3)
    p4 = (x4, y4)
    all_b, all_w = num_sq(1, 1, n, m)
    tmp = intc(p1, p2, p3, p4)
    if tmp:
        intc_1, intc_2 = tmp
        t_b, t_w = num_sq(intc_1[0], intc_1[1], intc_2[0], intc_2[1])
    b, w = num_sq(x1, y1, x2, y2)
    if tmp:
        b -= t_b
        w -= t_w
    b2, w2 = num_sq(x3, y3, x4, y4)
    if tmp:
        b2 -= t_b
        w2 -= t_w
    w_tot, b_tot = (all_w + b - w2, all_b - b + w2)
    if tmp:
        w_tot -= t_w
        b_tot += t_w
    print(w_tot, b_tot)
