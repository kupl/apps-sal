

from sys import stdin, stdout


def second_largest(numbers):
    count = 0
    m1 = m2 = float('-inf')
    for x in numbers:
        count += 1
        if x > m2:
            if x >= m1:
                m1, m2 = x, m1
                x_ind = count
            else:
                m2 = x
    return m2, x_ind if count >= 2 else None


def second_smallest(numbers):
    count = 0
    m1 = m2 = float('inf')
    for x in numbers:
        count += 1
        if x < m2:
            if x <= m1:
                m1, m2 = x, m1
                y_ind = count
            else:
                m2 = x
    return m2, y_ind if count >= 2 else None


n = int(stdin.readline())

x = []
y = []

for i in range(n):
    line = stdin.readline()
    a = list(map(int, line.split()))
    x.append(a[0])
    y.append(a[1])


x_max = max(x)

y_min = min(y)

x_max2, x_ind = second_largest(x)

y_min2, y_ind = second_smallest(y)

if x_ind == y_ind:
    print(max(y_min2 - x_max2, 0))
else:
    print(max((y_min2 - x_max), (y_min - x_max2), 0))
