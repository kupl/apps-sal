import sys

input_ = sys.stdin.readline


def is_ordered(arr):
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            return False
    else:
        return True


def main():
    n = int(input_())
    changed = False

    befores = []
    afters = []

    for x in range(n):
        before, after = list(map(int, input_().split()))

        if before != after:
            changed = True

        befores.append(before)
        afters.append(after)

    if changed:
        return "rated"

    if is_ordered(afters):
        return "maybe"

    return "unrated"


def __starting_point():
    print(main())

__starting_point()
