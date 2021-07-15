
def is_sorted(lst):
    it = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < it:
            return False
        it = lst[i]
    return True


def do(lst):
    if is_sorted(lst):
        return len(lst)

    v1 = do(lst[:len(lst) // 2])
    v2 = do(lst[len(lst) // 2:])

    return max(v1, v2)


N = int(input())

A = list(map(int, input().split()))
print(do(A))
