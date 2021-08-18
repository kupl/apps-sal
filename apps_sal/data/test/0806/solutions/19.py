import math


def main():
    n, l, r = (int(a) for a in input().split())
    mod = 10**9 + 7
    nums = [(math.floor(r / 3) - math.ceil(l / 3) + 1) % mod,
            (math.floor((r - 1) / 3) - math.ceil((l - 1) / 3) + 1) % mod,
            (math.floor((r - 2) / 3) - math.ceil((l - 2) / 3) + 1) % mod]
    rem = nums[:]
    for i in range(n - 1):
        newRem = []
        newRem.append(
            ((nums[0] * rem[0]) % mod +
             (nums[1] * rem[2]) % mod +
             (nums[2] * rem[1]) % mod) % mod
        )
        newRem.append(
            ((nums[0] * rem[1]) % mod +
             (nums[1] * rem[0]) % mod +
             (nums[2] * rem[2]) % mod) % mod
        )
        newRem.append(
            ((nums[0] * rem[2]) % mod +
             (nums[1] * rem[1]) % mod +
             (nums[2] * rem[0]) % mod) % mod
        )
        rem = newRem[:]
    print(rem[0])


main()
