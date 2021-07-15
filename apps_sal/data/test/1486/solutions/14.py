n = int(input())
cities = list(map(int, input().split()))
ends = [cities[0], cities[-1]]
for i in range(n):
    print(min(abs(cities[i - 1] - cities[i]), abs(cities[i + 1] - cities[i]) if i + 1 != n else float('inf')), max([abs(ends[j] - cities[i]) for j in range(2)]))

