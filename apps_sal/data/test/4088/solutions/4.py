T = int(input())
for _ in range(T):
    s = input()
    m = int(input())
    b = [int(s) for s in input().split()]
    count = [0] * 26
    for c in s:
        count[ord(c) - 97] += 1
    res = [''] * m
    p = 0
    while p < m:
        zeros = []
        for i in range(m):
            if b[i] == 0:
                zeros.append(i)
        for i in range(25,-1,-1):
            if count[i] >= len(zeros):
                c = chr(i + 97)
                count[i] = 0
                break
            else:
                count[i] = 0
        for zero in zeros:
            res[zero] = c
            b[zero] = -1
            for i in range(m):
                b[i] -= abs(i - zero)
        p += len(zeros)
    print(''.join(res))
