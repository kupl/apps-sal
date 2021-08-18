def main(nums):
    t = nums[0]
    for i in range(0, t + 1):
        q = nums[1]
        w = q - i
        e = t - i
        r = nums[2]
        f = w + e

        if r != f or w < 0:
            continue
        else:
            return '{} {} {}'.format(i, w, e)

    return 'Impossible'


def init():
    nums = list(map(int, input().split()))

    print(main(nums))


init()
