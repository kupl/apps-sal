N = int(input())
L = list(map(int, input().split()))[:N]
start = round(sum(L) / N)


def f(x):
    return (x - start) ** 2


print(sum(list(map(f, L))))
