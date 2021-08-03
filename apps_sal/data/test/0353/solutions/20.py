def ans(n, seq):
    if n == 1:
        if seq[0] == 0:
            return 'UP'
        elif seq[0] == 15:
            return 'DOWN'
        else:
            return -1
    elif seq[-1] == 15:
        return 'DOWN'
    elif seq[-1] == 0:
        return 'UP'
    elif seq[-1] > seq[-2] and seq[-1] != 15:
        return 'UP'
    elif seq[-1] < seq[-2] and seq[-1] != 0:
        return 'DOWN'


n = int(input())
seq = list(map(int, input().split()))
print(ans(n, seq))
