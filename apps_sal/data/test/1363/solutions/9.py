from math import factorial

n, m, k = (int(x) for x in input().split())
a = sorted([int(x) for x in input().split()])
b = sorted([int(x) for x in input().split()])
c = sorted([int(x) for x in input().split()])


def create_count_arr(a):
    a_count = [0] * (10 ** 5 + 5)
    for i in range(len(a)):
        a_count[a[i]:] = [i + 1] * ((10 ** 5 + 5) - a[i])
    return a_count


def get_num(x, y, a):
    if y >= len(a):
        y = len(a) - 1
    c = a[y] - a[x]
    if a[x] != a[x - 1]:
        c += 1
    return c


def num_of_permut(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


a_count = create_count_arr(a)
b_count = create_count_arr(b)
c_count = create_count_arr(c)

count = 0

for i in a:
    d = get_num(i, i * 2, b_count)
    f = get_num(i, i * 2, c_count)
    if d >= 2 and f >= 3:
        count += num_of_permut(d, 2) * num_of_permut(f, 3)
for i in b:
    g = get_num(i, i * 2, a_count)
    d = get_num(i, i * 2, b_count) - 1
    f = get_num(i, i * 2, c_count)
    if g >= 1 and d >= 1 and f >= 3:
        count += num_of_permut(d, 1) * num_of_permut(f, 3) * g

for i in c:
    g = get_num(i, i * 2, a_count)
    d = get_num(i, i * 2, b_count)
    f = get_num(i, i * 2, c_count) - 1
    if g >= 1 and d >= 2 and f >= 2:
        count += num_of_permut(d, 2) * num_of_permut(f, 2) * g

print(count)
