n = int(input())
l = [*map(int, input().split())]


def f(a):
    return [sum(min(
        [abs(e - a), abs(e - (a - 1)), abs(e - (a + 1))]) for e in l), a]


res = [float('inf'), float('inf')]
for a in range(1, 101):
    res = min(res, f(a))
print(res[1], res[0])
