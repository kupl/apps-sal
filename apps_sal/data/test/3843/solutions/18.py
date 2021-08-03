from itertools import permutations as p


def length_base_7(ele, arr):
    if not ele:
        arr.append(0)
        return 1
    length = 0
    while ele:
        arr.append(ele % 7)
        ele //= 7
        length += 1
    return length


n, m = list(map(int, input().split()))
n -= 1
m -= 1

n_base7, m_base7 = [], []
n_length, m_length = length_base_7(n, n_base7), length_base_7(m, m_base7)

n_base7, m_base7 = n_base7[::-1], m_base7[::-1]

combination_number = {0, 1, 2, 3, 4, 5, 6}
res = 0
for i in p(combination_number, n_length):
    if list(i) <= n_base7:
        for j in p(combination_number - set(i), m_length):
            if list(j) <= m_base7:
                res += 1

print(res)
