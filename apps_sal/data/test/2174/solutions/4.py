import sys
my_file = sys.stdin
n = int(my_file.readline())
a = [int(i) for i in my_file.readline().strip().split()]
a.sort()


def solve():
    turns = 0
    for i in range(1, n + 1):
        if a[i - 1] < i:
            turns += i - a[i - 1]
        elif a[i - 1] > i:
            turns += a[i - 1] - i
    return turns


print(solve())
