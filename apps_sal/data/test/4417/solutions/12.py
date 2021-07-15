q = int(input())

for i in range(q):
    n, k = [int(x) for x in input().split()]
    line = [int(x) for x in input().split()]

    if max(line) - min(line) > 2 * k:
        print(-1)
        continue
    else:
        print(min(line) + k)

