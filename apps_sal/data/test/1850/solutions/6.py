from bisect import bisect_right
(num_racers, selected_racer) = list(map(int, input().split()))
selected_racer -= 1
racers_points = list(map(int, input().split()))
selected_racer_points = racers_points[selected_racer]
awards = list(map(int, input().split()))
awards.sort(reverse=True)
selected_racer_points += awards[0]
remaining_awards = awards[1:]
del racers_points[selected_racer]
remaining_racers_points = sorted(racers_points, reverse=True)
best_award_pos = 0
worst_award_pos = len(remaining_awards) - 1
for (pos, racer_points) in enumerate(remaining_racers_points):
    if racer_points + remaining_awards[worst_award_pos] <= selected_racer_points:
        remaining_racers_points[pos] += remaining_awards[worst_award_pos]
        worst_award_pos -= 1
    else:
        remaining_racers_points[pos] += remaining_awards[best_award_pos]
        best_award_pos += 1
remaining_racers_points.append(selected_racer_points)
remaining_racers_points.sort()
print(num_racers + 1 - bisect_right(remaining_racers_points, selected_racer_points))
