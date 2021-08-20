import sys
lines = sys.stdin.readlines()
T = int(lines[0].strip())
for t in range(1, T + 1):
    n = int(lines[t].strip())
    if n % 4 == 2:
        print('NO')
        continue
    print('YES')
    res = []
    tmp = 0
    for i in range(1, n // 2 + 1):
        res.append(2 * i)
        tmp += 2 * i
    for i in range(1, n // 2):
        res.append(2 * i - 1)
        tmp -= 2 * i - 1
    res.append(tmp)
    print(' '.join(map(str, res)))
