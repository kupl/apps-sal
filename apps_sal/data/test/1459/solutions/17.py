def shortest_distance(n_station: int, distances: list, start: int, end: int) -> int:
    station_from = min(start, end)
    station_to = max(start, end)
    home = sum(distances[station_from:station_to])
    away = sum(distances[station_to:]) + sum(distances[:station_from])
    return min(home, away)


n = int(input())
d = [0] + [int(i) for i in input().split()]
(s, t) = map(int, input().split())
print(shortest_distance(n, d, s, t))
