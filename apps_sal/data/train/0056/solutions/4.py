import sys
lines = sys.stdin.readlines()
T = int(lines[0].strip())
for t in range(T):
    (a, b) = map(int, lines[t + 1].strip().split(" "))
    res = [[0 for _ in range(a)] for _ in range(a)]
    rema = b % a
    deno = b // a
    if rema == 0:
        val = 0
    else:
        val = 2
    for i in range(a):
        if i < rema:
            for j in range(deno + 1):
                res[i][(i + j) % a] = 1
        else:
            for j in range(deno):
                res[i][(i + j) % a] = 1
    print(val)
    for i in range(a):
        print(''.join(map(str, res[i])))
