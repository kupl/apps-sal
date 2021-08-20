import itertools
import math


def average_length():
    N = int(input())
    x = list()
    y = list()
    for _ in range(N):
        (X, Y) = map(int, input().split())
        x.append(X)
        y.append(Y)
    permutations_list = itertools.permutations([x for x in range(N)])
    all_case_distance_sum = 0
    for one_case in permutations_list:
        distance_sum = 0
        count = 0
        for i in one_case:
            count += 1
            if count == 1:
                pass
            else:
                D = (x[pass_num] - x[i]) ** 2 + (y[pass_num] - y[i]) ** 2
                d = math.sqrt(D)
                distance_sum += d
            pass_num = i
        all_case_distance_sum += distance_sum
    return all_case_distance_sum / math.factorial(N)


result = average_length()
print(result)
