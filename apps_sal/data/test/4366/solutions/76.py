(hour_a, hour_b) = list(map(int, input().split()))
contest_start_hour = 0
contest_start_hour = hour_a + hour_b
if contest_start_hour >= 24:
    contest_start_hour -= 24
print(contest_start_hour)
