N = int(input())
L = list(range(1, N + 1))
M = list(filter(lambda n: n % 3 != 0 and n % 5 != 0, L))
print(sum(M))
