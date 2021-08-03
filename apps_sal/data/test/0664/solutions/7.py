def is_sorted(a):
    for i in range(1, len(a)):
        if a[i - 1] > a[i]:
            return False
    return True


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    if is_sorted(a):
        return 0
    for i in range(1, len(a)):
        if a[i - 1] > a[i]:
            if is_sorted(a[i:] + a[:i]):
                return n - i
            else:
                return -1


print(solve())
