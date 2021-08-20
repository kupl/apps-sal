(n, x, y) = list(map(int, input().split()))
a = list(map(int, input().split()))


def is_not_so_rainy(n, x, y, a, i):
    for j in range(max(0, i - x), i):
        if a[j] <= a[i]:
            return False
    for j in range(i + 1, min(i + y + 1, n)):
        if a[j] <= a[i]:
            return False
    return True


def find_not_so_rainy(n, x, y, a):
    for i in range(n):
        if is_not_so_rainy(n, x, y, a, i):
            return i + 1
    return None


print(find_not_so_rainy(n, x, y, a))
