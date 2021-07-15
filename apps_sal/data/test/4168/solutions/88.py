N = int(input())


def max_pos_number(n):
    val = 0
    for i in range(n):
        if i % 2 == 0:
            val += 2**i
    return val


def min_pos_number(n):
    val = 0
    for i in range(n):
        if i % 2 == 1:
            val -= 2**i

    return val


n = 1
while True:
    if min_pos_number(n) <= N <= max_pos_number(n):
        break
    n += 1

result = []
for i in range(n-1, -1, -1):
    if i % 2 == 0:
        if N > max_pos_number(i):
            result.append(1)
            N -= (-2) ** i
        else:
            result.append(0)
    else:
        if N < min_pos_number(i):
            result.append(1)
            N -= (-2) ** i
        else:
            result.append(0)
print((''.join([str(x) for x in result])))

