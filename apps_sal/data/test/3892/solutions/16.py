(N, m) = [int(value) for value in input().split()]
candies = []
for _ in range(N):
    candies.append([])
for _ in range(m):
    (start, end) = [int(value) for value in input().split()]
    candies[start - 1].append(end - 1)
min_distantions = []
for start_pos in range(N):
    min_distantion = 0
    for shift in range(N):
        current_pos = (start_pos + shift) % N
        count_candies = len(candies[current_pos])
        if count_candies > 0:
            closest_candy = N - 1
            for candy_destination in candies[current_pos]:
                closest_candy = min(closest_candy, (N + candy_destination - current_pos) % N)
            min_distantion = max(min_distantion, closest_candy + shift + N * (count_candies - 1))
    min_distantions.append(min_distantion)
print(' '.join([str(distantion) for distantion in min_distantions]))
