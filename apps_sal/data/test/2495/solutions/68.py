import copy

n = int(input())
a = list(map(int, input().split()))


def f(org_a, odd):
    a = copy.copy(org_a)
    ans = 0
    if a[0] == 0:
        a[0] = 1 if odd else -1
        ans += 1
    elif a[0] > 0 and not odd:
        ans += a[0] + 1
        a[0] = -1
    elif a[0] < 0 and odd:
        ans += -a[0] + 1
        a[0] = 1
    current_sum = a[0]
    for i in range(1, len(a)):
        move = 0
        is_positive = current_sum > 0
        current_sum += a[i]
        if is_positive and current_sum >= 0:
            move = -current_sum - 1
        elif not is_positive and current_sum <= 0:
            move = -current_sum + 1

        current_sum += move
        a[i] += move
        ans += abs(move)
    return ans


print((min(f(a, True), f(a, False))))
