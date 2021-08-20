import sys
from operator import itemgetter


def count(a, b, num_a, num_b, cur_time):
    current_result = 0
    if num_a * a + num_b * b <= cur_time and cur_time >= 0:
        cur_time -= num_a * a + num_b * b
        current_result = num_a + num_b
        if num_a < total_a:
            if (total_a - num_a) * a <= cur_time:
                current_result += total_a - num_a
                cur_time -= (total_a - num_a) * a
            else:
                current_result += cur_time // a
                cur_time -= a * (cur_time // a)
        if num_b < total_b:
            if (total_b - num_b) * b <= cur_time:
                current_result += total_b - num_b
            else:
                current_result += cur_time // b
    return current_result


def solve(n, T, a, b, tasks, total_a, total_b):
    tasks = sorted(tasks)
    result = 0
    num_a = 0
    num_b = 0
    for i in range(len(tasks)):
        (time, t) = tasks[i]
        cur_time = time - 1
        current_result = count(a, b, num_a, num_b, cur_time)
        result = max(current_result, result)
        if t == 0:
            num_a += 1
        else:
            num_b += 1
        if i == len(tasks) - 1 or tasks[i + 1][1] != tasks[i][1]:
            result = max(result, count(a, b, num_a, num_b, cur_time))
    result = max(result, count(a, b, total_a, total_b, T))
    return result


q = int(input())
for i in range(q):
    (n, T, a, b) = list(map(int, input().split()))
    types = list(map(int, input().split()))
    (total_a, total_b) = (0, 0)
    for t in types:
        if t == 0:
            total_a += 1
        else:
            total_b += 1
    t = list(map(int, input().split()))
    tasks = list(zip(t, types))
    print(solve(n, T, a, b, tasks, total_a, total_b))
