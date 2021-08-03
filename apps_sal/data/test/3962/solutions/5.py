print(sum([max(*x) + 1 for x in zip(*list(map(sorted, list(zip(*[list(map(int, input().split())) for _ in range(int(input()))])))))]))
