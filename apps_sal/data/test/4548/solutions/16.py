def tool_gate(now: int, gate_list: list) -> int:
    back_count = sum((i < now for i in gate_list))
    forward_count = sum((i > now for i in gate_list))
    return min(back_count, forward_count)


def __starting_point():
    (n, m, now) = list(map(int, input().split()))
    gate_list = list(map(int, input().split()))
    print(tool_gate(now, gate_list))


__starting_point()
