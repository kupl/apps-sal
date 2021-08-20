(n, m) = [int(x) for x in input().split()]
a = input()
b = input()
if '*' not in a:
    if a == b:
        print('YES')
    else:
        print('NO')
else:
    (part1, part2) = a.split('*')
    if b.startswith(part1) and b.endswith(part2) and (len(part1) + len(part2) <= len(b)):
        print('YES')
    else:
        print('NO')
