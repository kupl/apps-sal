n = int(input())

if (n == 3):
    print('1 1 3')
else:
    done = 0
    arr = []
    for i in range(30, -1, -1):
        arr.extend([2**i] * (n // (2**i) - done))
        done += n // (2**i) - done
        if (done == 1):
            k = i

    arr[0] = max(arr[0], (n // 2**(k - 1)) * 2**(k - 1))

    arr.reverse()
    print(' '.join(map(str, arr)))
