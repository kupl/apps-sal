n, m, k = list(map(int, input().split()))
holes = list(map(int, input().split()))

is_hole = [False for i in range(n)]

for i in holes:
    is_hole[i - 1] = True

bone = 0

if is_hole[0]:
    print(1)
else:
    was = False
    for i in range(k):
        a, b = list(map(int, input().split()))
        a -= 1
        b -= 1
        if a == bone:
            bone = b
        elif b == bone:
            bone = a
        if is_hole[bone]:
            was = True
            print(bone + 1)
            break
    if not was:
        print(bone + 1)
