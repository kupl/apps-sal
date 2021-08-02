n = int(input())
arr = [int(x) for x in input().split()]


def get_for(x):
    nonlocal n, arr

    ret = 0
    for i in range(n):
        ret += (abs(x - i) + i + x) * arr[i] * 2

    return ret


mn = get_for(0)
for i in range(1, n):
    mn = min(mn, get_for(i))

print(mn)
