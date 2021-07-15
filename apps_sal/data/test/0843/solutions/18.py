def __starting_point():
    n = int(input())
    ins = list(str(input()))
    abi = list(map(int, input().split()))
    sta = [False] * n
    pos = 0
    while True:
        sta[pos] = True
        if ins[pos] == '>':
            pos += abi[pos]
        elif ins[pos] == '<':
            pos -= abi[pos]
        if pos < 0 or pos > n - 1:
            print('FINITE')
            break
        elif sta[pos]:
            print('INFINITE')
            break

__starting_point()
