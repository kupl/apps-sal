import sys


def nline():
    return sys.stdin.readline()[:-1]


def ni():
    return int(sys.stdin.readline())


def na():
    return [int(v) for v in sys.stdin.readline().split()]


(n, m) = na()
arr = na()
sm = 0
count = [0] * 101
for i in range(0, n):
    (diff, k) = (sm + arr[i] - m, 0)
    if diff > 0:
        for j in range(100, -1, -1):
            tmp = count[j] * j
            if tmp >= diff:
                k += (diff + j - 1) // j
                break
            k += count[j]
            diff -= tmp
    print(k, end=' ')
    sm += arr[i]
    count[arr[i]] += 1
