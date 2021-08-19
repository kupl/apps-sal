(n, m) = list(map(int, input().split()))
k = 1
k_even = n // 2 + 1
p_even = k_even + 1


def rotate(s, diff):
    if s + diff < 1:
        return s + diff + n
    elif s + diff > n:
        return s + diff - n
    return s + diff


for i in range(m + 1):
    if i != 0 and i % 2 == 0:
        print((rotate(k, -(i // 2)), rotate(k, i // 2)))
    if i % 2 == 1:
        print((rotate(k_even, -(i // 2)), rotate(p_even, i // 2)))
