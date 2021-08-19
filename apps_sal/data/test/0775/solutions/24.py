(n, m, k) = [int(x) for x in input().strip().split(' ')]
holes = set([int(x) for x in input().strip().split(' ')])
bone = 1
fall = bone in holes
i = 0
while i < k and (not fall):
    (a, b) = [int(x) for x in input().strip().split(' ')]
    if a == bone:
        bone = b
    elif b == bone:
        bone = a
    fall = bone in holes
    i += 1
print(bone)
