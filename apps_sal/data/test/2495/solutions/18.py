N = int(input())
A = list(map(int, input().split()))


def sequence(plus_start):
    cost = 0
    cum = 0

    for i in range(N):
        tmp = cum + A[i]
        target = tmp
        if plus_start:
            if i % 2 == 0:
                if tmp <= 0:
                    target = 1
            else:
                if tmp >= 0:
                    target = -1
        else:
            if i % 2 == 0:
                if tmp >= 0:
                    target = -1
            else:
                if tmp <= 0:
                    target = 1
        diff = target - tmp
        cum += A[i] + diff
        cost += abs(diff)
    return cost


print((min(sequence(True), sequence(False))))
