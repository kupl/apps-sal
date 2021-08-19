import sys
for _ in range(int(sys.stdin.readline().rstrip())):
    (a, b, c) = list(map(int, sys.stdin.readline().rstrip().split()))
    re = 99999999
    re_arr = [a, b, c]
    for i in range(1, 10001):
        chk_i = abs(i - a)
        if chk_i > re and i > a:
            break
        j = 1
        while True:
            chk_j = chk_i + abs(b - i * j)
            if chk_j > re and i * j > b:
                break
            k = 1
            while True:
                chk_k = chk_j + abs(c - i * j * k)
                if chk_k > re and i * j * k > c:
                    break
                elif chk_k < re:
                    re = chk_k
                    re_arr = [i, i * j, i * j * k]
                k += 1
            j += 1
    print(re)
    for i in re_arr:
        print(i, end=' ')
    print('')
