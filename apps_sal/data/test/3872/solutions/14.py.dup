def reorder(a):
    length = len(a)
    if length % 2 == 1:
        return a
    else:
        return sorted([reorder(a[:length // 2]), reorder(a[length // 2:])])


if reorder(input()) == reorder(input()):
    print("YES")
else:
    print("NO")
