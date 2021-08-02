def main(n, nums):
    ex = n // 3
    if 5 in nums or 7 in nums or nums.count(1) != ex:
        return -1
    else:
        s = ''
        q = nums.count(4)
        w = nums.count(6)
        e = nums.count(3)
        r = nums.count(2)
        if r != q + w - e or w != e + r - q or e > w or q > r:
            return -1
        s += '1 2 4\n' * q
        s += '1 2 6\n' * (ex - q - e)
        s += '1 3 6\n' * e
        return s[:-1]


def init():
    n = int(input())
    nums = list(map(int, input().split()))

    print(main(n, nums))


init()
