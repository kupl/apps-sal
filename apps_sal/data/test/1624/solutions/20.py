import random


def ii():
    return int(input())


def mi():
    return list(map(int, input().split()))


def li():
    return list(mi())


n = ii()
a = li()
random.shuffle(a)
a = sorted(a)
ans = 0
for i in range(n // 2):
    ans += pow(a[i] + a[n - i - 1], 2)
print(ans)
