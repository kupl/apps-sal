q = int(input())
for _ in range(q):
    n, k = map(int, input().split())

    line = list(input())

    zero = 0
    non_zero = 0
    while zero < n:
        if line[zero] != '0':
            zero += 1
            continue
        pos = zero
        if zero - non_zero < k:
            k -= zero - non_zero
            line[zero] = '1'
            line[non_zero] = '0'
            non_zero += 1
        else:
            line[zero - k] = '0'
            line[zero] = '1'
            break
        if k == 0:
            break
        zero += 1
    print(*line, sep="")
