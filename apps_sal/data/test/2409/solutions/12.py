import sys
inpy = [int(x) for x in sys.stdin.read().split()]
t = inpy[0]
index = 1
for _ in range(t):
    n, k, l = inpy[index], inpy[index + 1], inpy[index + 2]
    index += 3
    d = inpy[index:index + n]

    index += n
    x, m = k, True
    flag = True
    for i in range(n):
        diff = l - d[i]

        if diff < 0:
            flag = False
            break
        if diff >= k:
            x = k
            m = True
        else:
            if m:
                x = min(x - 1, diff)
                if x == 0:
                    m = False
            else:
                x = x + 1
                if x > diff:
                    flag = False
                    break
    if flag:
        print('Yes')
    else:
        print('No')
