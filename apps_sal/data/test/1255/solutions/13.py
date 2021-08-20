n = int(input())
arrivals_count = {}
for _ in range(n):
    arrival = input()
    arrivals_count[arrival] = arrivals_count.get(arrival, 0) + 1
print(max(arrivals_count.values()))
