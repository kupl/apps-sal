
n, d = list(map(int, input().split()))

result, current = 0, 0

for _ in range(d):
    tmp = input()
    if any([x != '1' for x in tmp]):
        current += 1
    else:
        result = max([result, current])
        current = 0

result = max([result, current])
print(result)
