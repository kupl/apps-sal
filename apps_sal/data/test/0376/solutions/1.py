n = int(input())

strengths = list(map(int, input().split()))
max_strength = max(strengths)

count_max = strengths.count(max_strength)
count_second_place = strengths.count(max_strength - 1)

maxes = [0 for i in range(n)]
second_places = [0 for i in range(n)]

for i in range(n - 1):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    if strengths[a] == max_strength:
        maxes[b] += 1
    elif strengths[a] == max_strength - 1:
        second_places[b] += 1

    if strengths[b] == max_strength:
        maxes[a] += 1
    elif strengths[b] == max_strength - 1:
        second_places[a] += 1

total_max = 1000000009
for i in range(n):
    here = 0
    if strengths[i] < max_strength:
        if maxes[i] == count_max:
            here = max_strength + 1
        else:
            here = max_strength + 2
    else:
        if count_max == 1:
            if second_places[i] == count_second_place:
                here = max_strength
            else:
                here = max_strength + 1
        else:
            if maxes[i] == count_max - 1:
                here = max_strength + 1
            else:
                here = max_strength + 2
    total_max = min(total_max, here)

print(total_max)
