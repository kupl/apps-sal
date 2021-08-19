import numpy as np
from collections import Counter
YEAR = 2019


def solve(S: str):
    mod_year = np.arange(1, 10)
    mod_s = []
    for Si in map(int, reversed(S)):
        mod_s.append(mod_year[Si - 1])
        mod_year = mod_year * 10 % YEAR
    cum_sum = 0
    cum_sums = [cum_sum]
    for x in mod_s:
        cum_sum = (cum_sum + x) % YEAR
        cum_sums.append(cum_sum)
    answer = 0
    for (_, num) in list(Counter(cum_sums).items()):
        answer += num * (num - 1) // 2
    return answer


def main():
    S = input().strip()
    answer = solve(S)
    print(answer)


def __starting_point():
    main()


__starting_point()
