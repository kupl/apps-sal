k = int(input())


def digit_sum(s):
    return sum(map(int, list(s)))


def func1(s):
    return int(s) / digit_sum(s)


def func2(n):
    n = str(n)
    fm, fa = float("inf"), -1
    for i in range(len(n)):
        s = n[:i + 1] + "9" * (len(n) - i - 1)
        if fm > func1(s):
            fm = func1(s)
            fa = int(s)
    return fa


n = 1
for _ in range(k):
    print(n)
    n = func2(n + 1)
