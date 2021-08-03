N = int(input())
K = int(input())
X = list([int(x) for x in input().split()])

result = 0

for pos in X:
    if pos <= abs(pos - K):
        result += 2 * pos
    else:
        result += 2 * abs(pos - K)

print(result)
