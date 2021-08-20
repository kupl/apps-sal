import sys
test_count = int(sys.stdin.readline())
for test in range(test_count):
    sys.stdin.readline()
    (m, k) = list(map(int, sys.stdin.readline().split()))
    counts = list(map(int, sys.stdin.readline().split()))
    took = []
    unhappy = []
    for i in range(m - 1):
        (t, r) = list(map(int, sys.stdin.readline().split()))
        t -= 1
        took.append(t)
        unhappy.append(r)
    took_in_total = [0 for dish_count in counts]
    for i in range(m - 1):
        if took[i] != -1:
            took_in_total[took[i]] += 1
    took_already = [0 for dish_count in counts]
    left = [dish_count for dish_count in counts]
    answer = [False for dish_count in counts]
    unknown = 0
    all_present = True
    for i in range(m - 1):
        if unhappy[i] == 1 and all_present:
            could_exhaust = []
            for j in range(k):
                if took_already[j] < took_in_total[j]:
                    continue
                if left[j] > unknown:
                    continue
                could_exhaust.append(j)
            if len(could_exhaust) == 0:
                raise AssertionError
            for j in could_exhaust:
                answer[j] = True
            unknown -= min([left[j] for j in could_exhaust])
            all_present = False
        if took[i] != -1:
            left[took[i]] -= 1
            took_already[took[i]] += 1
            if left[took[i]] == 0:
                all_present = False
        else:
            unknown += 1
    for j in range(k):
        if left[j] <= unknown:
            answer[j] = True
    sys.stdout.write(''.join(['Y' if x else 'N' for x in answer]) + '\n')
