def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def check(m):
    nonlocal n, arr, x, a, y, b, k

    arr2 = arr[:m]
    count_double = m // (a * b // gcd(a, b))
    maximals = sorted(arr, reverse=True)[:(m // a + m // b - count_double)]
    ans = 0
    for i in maximals[:count_double]:
        ans += (x + y) * i
    maximals = maximals[count_double:]

    count_a = m // a - count_double
    count_b = m // b - count_double
    for i in maximals[:count_a]:
        ans += x * i
    for i in maximals[count_a:]:
        ans += y * i

    return ans >= k


Q = int(input())

for q in range(Q):
    n = int(input())
    arr = list(map(int, input().split()))
    arr = [i // 100 for i in arr]
    x, a = tuple(map(int, input().split()))
    y, b = tuple(map(int, input().split()))
    k = int(input())

    if x < y:
        x, a, y, b = y, b, x, a

    left = 0
    right = n
    medium = 0
    while right - left > 1:
        medium = (left + right) // 2

        if check(medium):
            right = medium
        else:
            left = medium

    if check(left):
        print(left)
    elif check(medium):
        print(medium)
    elif check(right):
        print(right)
    else:
        print(-1)
'''
    count_double = n // (a * b // gcd(a, b))
    #print(n // a + n // b - count_double)
    maximals = sorted(arr, reverse=True)[:(n // a + n // b - count_double)]
    ans = 0
    for i in maximals[:count_double]:
        ans += (x + y) * i
    maximals = maximals[count_double:]

    count_a = n // a - count_double
    count_b = n // b - count_double
    for i in maximals[:count_a]:
        ans += x * i
    for i in maximals[count_a:]:
        ans += y * i

    print(ans, k, ans >= k)
'''
