def count_biscuits_num() -> int:
    after_a_sec, making_per_a, until_sec = map(int, input().split())
    limited_time = float(until_sec) + 0.5
    spent_time = after_a_sec
    total_making = 0

    while True:
        if limited_time >= spent_time:
            total_making += making_per_a
            spent_time += after_a_sec
        else:
            return total_making


print(count_biscuits_num())
