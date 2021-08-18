
def can_order(arr, ok):
    i = 0
    while i < len(ok):
        if not ok[i]:
            if i + 1 != arr[i + 1] and (i + 1 >= len(ok) or not ok[i + 1]):
                return False
            i += 1
        else:
            j = i
            while j < len(ok) and ok[j]:
                j += 1
            if sum(arr[i:j + 1]) != sum(range(i, j + 1)):
                return False
            i = j
    return True


def main():
    N = int(input())
    arr = [int(x) - 1 for x in input().split()]
    ok = [c == '1' for c in input()]
    print("YES" if can_order(arr, ok) else "NO")


def __starting_point():
    main()


__starting_point()
