def input_persons() -> dict:
    n = int(input())
    result = {'length': n, 'hour': [], 'minute': []}
    for _ in range(n):
        (h, m) = map(int, input().split())
        result['hour'].append(h)
        result['minute'].append(m)
    return result


def count_cash(arrivals: dict) -> int:
    min_cash = 0
    i = 0
    while i < arrivals['length']:
        j = i
        while j < arrivals['length'] - 1 and arrivals['hour'][j + 1] == arrivals['hour'][j] and (arrivals['minute'][j + 1] == arrivals['minute'][j]):
            j += 1
        cash = j - i + 1
        if cash > min_cash:
            min_cash = cash
        i = j + 1
    return min_cash


print(count_cash(input_persons()))
