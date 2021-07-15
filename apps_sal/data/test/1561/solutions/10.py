n, m, k = (int(x) for x in input().split())

COLCON = [0 for _ in range(m)]

res = 0
for _ in range(n):
    con = 0

    for i, c in enumerate(input().strip()):
        if c == '*':
            con = 0
            COLCON[i] = 0

        else:
            con += 1
            if con >= k:
                res += 1

            COLCON[i] += 1
            if COLCON[i] >= k:
                res += 1

if k == 1:
    print(res // 2)
else:
    print(res)
