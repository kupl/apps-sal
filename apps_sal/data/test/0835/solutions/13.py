recipe = input()
n_b, n_s, n_c = list(map(int, input().split()))
p_b, p_s, p_c = list(map(int, input().split()))
money = int(input())

c_b, c_s, c_c = recipe.count('B'), recipe.count('S'), recipe.count('C')


def calc_cost(count):
    return max(0, count * c_b - n_b) * p_b + max(0, count * c_s - n_s) * p_s + max(0, count * c_c - n_c) * p_c


def find_answer():
    l, r = 0, 10**13
    while l + 1 < r:
        mid = (l + r) // 2
        mid_val = calc_cost(mid)
        if mid_val > money:
            r = mid
        else:
            l = mid
    return l


print(find_answer())
