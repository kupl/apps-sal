import math


def hats(n, arr):
    processed = [False] * n
    hats = [None] * n
    cur_hat = 0
    for (i, diff_count) in enumerate(arr):
        if processed[i]:
            continue
        cur_hat += 1
        hats[i] = cur_hat
        processed[i] = True
        same_count = n - diff_count - 1
        if not same_count:
            continue
        for j in range(i + 1, n):
            if arr[j] == diff_count:
                same_count -= 1
                processed[j] = True
                hats[j] = cur_hat
            if not same_count:
                break
        if same_count:
            print('Impossible')
            return
    print('Possible')
    print(' '.join(list(map(str, hats))))


def __starting_point():
    n = int(input())
    answers = list(map(int, input().strip().split()))
    hats(n, answers)


__starting_point()
