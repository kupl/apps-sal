def shortest_distance(distances: list, start: int, end: int) -> int:
    if start > end:
        (start, end) = (end, start)
    home = sum(distances[start:end])
    away = sum(distances[end:]) + sum(distances[:start])
    return min(home, away)


input()
d = [0] + [int(i) for i in input().split()]
(s, t) = map(int, input().split())
print(shortest_distance(d, s, t))
