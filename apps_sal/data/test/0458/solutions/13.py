solutions = []
(a, b, c) = list(map(int, input().split(' ')))
for s in range(1, 82):
    x = b * s ** a + c
    if 0 < x < 10 ** 9:
        if sum(map(int, list(str(x)))) == s:
            solutions.append(x)
print(len(solutions))
print(' '.join(map(str, solutions)))
