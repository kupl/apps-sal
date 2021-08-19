import sys


def main():
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    total_sum = sum(a)
    if n == 1:
        print(1 - sum(a))
        return
    max_sum = total_sum
    for i in range(n):
        for j in range(i + 1, n + 1):
            new_sum = total_sum + j - i - 2 * sum(a[i:j])
            if new_sum > max_sum:
                max_sum = new_sum
    if max_sum == total_sum:
        max_sum -= 1
    print(max_sum)


def __starting_point():
    return main()


__starting_point()
