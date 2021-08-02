N, M = map(int, input().split())
cakes = tuple(tuple(map(int, input().split())) for _ in range(N))


def make_function(i):
    return lambda t: sum(t[j] * (-1) ** ((i >> j) & 1) for j in range(3))


functions = [make_function(i) for i in range(8)]
print(max(map(sum, (sorted((function(cake) for cake in cakes), reverse=True)[:M] for function in functions))))
