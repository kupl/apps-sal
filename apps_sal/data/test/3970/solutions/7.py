from sys import stdin


def main():
    """
    Name: Kevin S. Sanchez
    Code: A. k-Multiple Free Set
    """
    inp = stdin
    (n, k) = list(map(int, inp.readline().split()))
    nums = list(map(int, inp.readline().split()))
    nums.sort(reverse=True)
    final = set()
    for i in range(0, n):
        mult = nums[i] * k
        if not mult in final:
            final.add(nums[i])
    print(len(final))


main()
