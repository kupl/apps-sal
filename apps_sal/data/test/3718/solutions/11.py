def judge(balls):
    if len(balls) < 3:
        return False
    candidates = set()
    counter = 1
    sorted_balls = sorted(balls)
    prev_ball = sorted_balls.pop(0)
    for ball in sorted_balls:
        if prev_ball + 1 == ball:
            counter += 1
        else:
            candidates.add(counter)
            counter = 1
        prev_ball = ball
    candidates.add(counter)
    return max(candidates) >= 3


def main():
    _ = input()
    balls = set(map(int, input().split()))
    if judge(balls):
        print('YES')
    else:
        print('NO')


def __starting_point():
    main()


__starting_point()
