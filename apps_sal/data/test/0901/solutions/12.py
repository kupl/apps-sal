

n, m = list(map(int, input().split()))

dont_end = True

for _ in range(m):
    k, *elements = list(map(int, input().split()))
    some_set = set(elements)
    good = False
    for x in some_set:
        if (-x) in some_set:
            good = True
            break
    if not good:
        dont_end = False

if dont_end:
    print("NO")
else:
    print("YES")
