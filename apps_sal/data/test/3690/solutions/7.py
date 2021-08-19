def __starting_point():
    (h, m, s, t1, t2) = [int(x) for x in input().split()]
    hand_angles = [s / 60 * 360, (m + s / 60) / 60 * 360, (h % 12 + m / 60 + s / 3600) / 12 * 360]
    t1_angle = t1 % 12 / 12 * 360
    t2_angle = t2 % 12 / 12 * 360
    if t1_angle > t2_angle:
        (t1_angle, t2_angle) = (t2_angle, t1_angle)
    can_go_clockwise = True
    can_go_counterclockwise = True
    for angle in hand_angles:
        if angle > t1_angle and angle < t2_angle:
            can_go_clockwise = False
        if not (angle >= t1_angle and angle <= t2_angle):
            can_go_counterclockwise = False
    print('YES' if can_go_clockwise or can_go_counterclockwise else 'NO')


__starting_point()
