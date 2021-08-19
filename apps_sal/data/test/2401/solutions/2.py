def main():
    T = int(input())
    for _ in range(T):
        (n, r) = readints()
        nums = readints()
        print(sol(nums, r, n))


def readints():
    return [int(fld) for fld in input().strip().split()]


def sol(nums, r, n):
    ans = 1 + (r - sum(nums)) % n
    return ans


main()
