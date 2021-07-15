x, y, l, r = list(map(int, input().split()))


def gen_list(var):
    cur = 1
    while cur <= r:
        yield cur
        cur *= var

x_list = list(gen_list(x))
# print(x_list)
y_list = list(gen_list(y))
# print(y_list)

numbers = [l-1, r+1]
for _x in x_list:
    for _y in y_list:
        n = _x + _y
        if n < l or n > r:
            continue
        numbers.append(n)

numbers = sorted(set(numbers))
# print(numbers)

if len(numbers) < 2:
    print('0')
    return

max_happy = max([numbers[i+1]-numbers[i]-1 for i in range(len(numbers) - 1)], default=0)

print(max_happy)

