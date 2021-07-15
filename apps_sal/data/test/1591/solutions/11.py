from math import ceil
n, k = map(int, input().split())
drinks = [False for i in range(k + 1)]
satisfied = 0
for i in range(n):
    d = int(input())
    if drinks[d]:
        satisfied += 2
    drinks[d] = not drinks[d]
unsat = len(list(filter(lambda x: x, drinks)))
print(satisfied + ceil(unsat / 2))
