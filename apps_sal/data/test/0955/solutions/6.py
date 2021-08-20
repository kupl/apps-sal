import sys


def __starting_point():
    n = int(next(sys.stdin))
    optimal = {ele: float('inf') for ele in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1)]}
    optimal[0, 0, 0] = 0
    for _ in range(n):
        (price, vitamin) = next(sys.stdin).strip().split()
        price = int(price)
        state = (int('A' in vitamin), int('B' in vitamin), int('C' in vitamin))
        for a in range(2):
            for b in range(2):
                for c in range(2):
                    if optimal[a, b, c] < float('inf'):
                        new_state = (a | state[0], b | state[1], c | state[2])
                        optimal[new_state] = min(optimal[new_state], optimal[a, b, c] + price)
    print(-1 if optimal[1, 1, 1] == float('inf') else optimal[1, 1, 1])


__starting_point()
