from itertools import permutations

n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
a_r, a_s, a_p = a
b_r, b_s, b_p = b
a_max_win = 0
k = min(a_r, b_s)
a_max_win += k
a_r -= k
b_s -= k
k = min(a_s, b_p)
a_max_win += k
a_s -= k
b_p -= k
k = min(a_p, b_r)
a_max_win += k
a_p -= k
b_r -= k

a_r, a_s, a_p = b
b_r, b_s, b_p = a


def simulate(a__r, a__s, a__p, b__r, b__s, b__p, order):
    for i in order:
        if i == 0:
            k = min(a__r, b__s)
            a__r -= k
            b__s -= k
        elif i == 1:
            k = min(a__s, b__p)
            a__s -= k
            b__p -= k
        elif i == 2:
            k = min(a__p, b__r)
            a__p -= k
            b__r -= k
        elif i == 3:
            k = min(a__r, b__r)
            a__r -= k
            b__r -= k
        elif i == 4:
            k = min(a__s, b__s)
            a__s -= k
            b__s -= k
        else:
            k = min(a__p, b__p)
            a__p -= k
            b__p -= k
    return sum([a__r, a__s, a__p])


print(min(simulate(a_r, a_s, a_p, b_r, b_s, b_p, p) for p in permutations(list(range(6)))), a_max_win)

