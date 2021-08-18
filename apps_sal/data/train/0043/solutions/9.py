import sys
input = iter(sys.stdin.read().splitlines()).__next__

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    times = list(zip(a, b))
    times.sort()
    pickup_time = sum(b)
    best_time = pickup_time
    for num_deliveries in range(1, n + 1):
        pickup_time -= times[num_deliveries - 1][1]
        delivery_time = times[num_deliveries - 1][0]
        best_time = min(best_time, max(pickup_time, delivery_time))
        if pickup_time < delivery_time:
            break
    print(best_time)
