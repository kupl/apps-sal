from collections import Counter
n = int(input())
a = list(map(int, input().split()))

# 矛盾チェック
c = Counter(a)


def check():
    if n & 1:
        if c[0] != 1:
            return False
        for i in range((n - 1) // 2):
            if c[2 * (i + 1)] != 2:
                return False
    else:
        for i in range(n // 2):
            if c[2 * i + 1] != 2:
                return False
    return True


if not check():
    print(0)
    return

print(pow(2, n // 2, 10**9 + 7))
