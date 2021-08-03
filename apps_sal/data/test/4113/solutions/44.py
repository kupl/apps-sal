n = int(input())


def f():
    for i in range(100):
        for j in range(100):
            if 4 * i + 7 * j == n:
                return "Yes"
    return "No"


print(f())
