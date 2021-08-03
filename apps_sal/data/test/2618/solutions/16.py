import math

t = int(input())


def check(mid):
    nonlocal n, p, x, a, y, b, k
    result = 0
    best = mid // (a * b // math.gcd(a, b))
    best_a = mid // a
    best_b = mid // b
    kolvo = 0
    for i in range(best):
        if kolvo == mid:
            break
        result += (p[n - i - 1] // 100) * (x + y)
        kolvo += 1
    if x > y:
        for i in range(best_a - best):
            if kolvo == mid:
                break
            result += (p[n - i - best - 1] // 100) * x
            kolvo += 1
        for i in range(best_b - best):
            if kolvo == mid:
                break
            result += (p[n - i - (best_a - best) - best - 1] // 100) * y
            kolvo += 1
    else:
        for i in range(best_b - best):
            if kolvo == mid:
                break
            result += (p[n - i - best - 1] // 100) * y
            kolvo += 1
        for i in range(best_a - best):
            if kolvo == mid:
                break
            result += (p[n - i - (best_b - best) - best - 1] // 100) * x
            kolvo += 1
    if result >= k:
        return True
    return False

    if result >= k:
        return True
    return False


for i in range(t):
    n = int(input())
    p = [int(i) for i in input().split()]
    x, a = list(map(int, input().split()))
    y, b = list(map(int, input().split()))
    k = int(input())
    p.sort()
    left = 0
    right = n
    while (right - left > 1):
        middle = (left + right) // 2
        if check(middle):
            right = middle
        else:
            left = middle
    if check(left):
        print(left)
    elif check(right):
        print(right)
    else:
        print(-1)
