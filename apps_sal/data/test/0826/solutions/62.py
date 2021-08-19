n = int(input())


def possible(x):
    if (1 + x) * x <= 2 * (n + 1):
        return True
    else:
        return False


left = 0
right = 10 ** 10
while right - left > 1:
    middle = (right + left) // 2
    if possible(middle):
        left = middle
    else:
        right = middle
print(n + 1 - left)
