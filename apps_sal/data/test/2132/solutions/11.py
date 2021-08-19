def Task485D():
    cur_speed = 0
    is_outstrip = 0
    err_count = 0
    event_speed_limit = []
    event_count = int(input())
    for a in range(event_count):
        ev = list(map(int, input().split()))
        if ev[0] == 1:
            cur_speed = ev[1]
            while len(event_speed_limit) > 0:
                if cur_speed > event_speed_limit[len(event_speed_limit) - 1]:
                    event_speed_limit.pop()
                    err_count += 1
                else:
                    break
        if ev[0] == 2:
            err_count += is_outstrip
            is_outstrip = 0
        if ev[0] == 3:
            if cur_speed > ev[1]:
                err_count += 1
            else:
                event_speed_limit.append(ev[1])
        if ev[0] == 4:
            is_outstrip = 0
        if ev[0] == 5:
            event_speed_limit.clear()
        if ev[0] == 6:
            is_outstrip += 1
    print(err_count)


def __starting_point():
    Task485D()


__starting_point()
