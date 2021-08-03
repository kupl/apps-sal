
m = int(input())
for i in range(m):
    n, T, a, b = list(map(int, input().split()))
    is_hard = list(map(int, input().split()))
    total_hard = sum(is_hard)
    total_easy = n - total_hard
    time_mandatory = list(map(int, input().split()))
    mandatory_times = sorted([(time_mandatory[i], i)
                              for i in range(len(time_mandatory))])
    mandatory_times.append((T, -1))
    maximal_points = 0
    min_easy = 0
    min_hard = 0
    for (i, (time, problem_no)) in enumerate(mandatory_times):
        bad = False
        if i != len(mandatory_times) - 1 and mandatory_times[i + 1][0] == time:
            bad = True
        remaining_easy = total_easy - min_easy
        remaining_hard = total_hard - min_hard
        remaining_time = time - 1 - min_easy * a - min_hard * b
        if remaining_time >= 0:
            if remaining_time >= a * remaining_easy:
                maximal_points = max(maximal_points,
                                     min_easy + min_hard + remaining_easy +
                                     min((remaining_time - a * remaining_easy) // b,
                                           remaining_hard))
            else:
                maximal_points = max(maximal_points,
                                     min_easy + min_hard + remaining_time // a)
        if problem_no == -1:
            min_easy = min_easy
        elif is_hard[problem_no] == 1:
            min_hard += 1
        else:
            min_easy += 1
        if bad:
            continue
        remaining_easy = total_easy - min_easy
        remaining_hard = total_hard - min_hard
        remaining_time = time - min_easy * a - min_hard * b
        if remaining_time >= 0:
            if remaining_time >= a * remaining_easy:
                maximal_points = max(maximal_points,
                                     min_easy + min_hard + remaining_easy +
                                     min((remaining_time - a * remaining_easy) // b,
                                           remaining_hard))
            else:
                maximal_points = max(maximal_points,
                                     min_easy + min_hard + remaining_time // a)
    print(maximal_points)
