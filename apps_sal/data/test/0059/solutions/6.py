def check(vals, allowed):
    groups = []
    group = []
    for (v, b) in zip(vals, allowed):
        group.append(v)
        if b == '0':
            group.sort()
            groups.append(group)
            group = []
    flat = [v for group in groups for v in group]
    for i in range(1, len(flat)):
        if flat[i] < flat[i - 1]:
            return False
    return True


n = int(input())
vals = [int(v) for v in input().split()]
allowed = input().strip() + '0'
print(['NO', 'YES'][check(vals, allowed)])
