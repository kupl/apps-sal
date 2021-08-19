import itertools


def read_ints():
    return list(map(int, input().strip().split()))


def read_int():
    return read_ints()[0]


def check(nums, step, pre):
    suma = 0
    for x in nums:
        s = pre - x
        if abs(step - s) > 1:
            raise Exception()
        if step == s:
            pre = x
            continue
        suma += 1
        if pre - (x + 1) == step:
            pre = x + 1
        else:
            pre = x - 1
    return suma


def main():
    n = read_int()
    nums = read_ints()
    if n <= 2:
        print(0)
        return
    suma = 100000000
    for (x, y) in itertools.product([-1, 0, 1], [-1, 0, 1]):
        a = nums[0] + x
        b = nums[1] + y
        diff = a - b
        try:
            suma = min(suma, check(nums[2:], diff, b) + abs(x) + abs(y))
        except Exception as e:
            pass
    if suma == 100000000:
        print(-1)
    else:
        print(suma)


main()
